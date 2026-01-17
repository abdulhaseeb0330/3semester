import React, { useState, useEffect } from 'react';
import {
  View, Text, StyleSheet, FlatList, TouchableOpacity, 
  TextInput, Modal, Dimensions, ScrollView, Alert, Image
} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { LineChart } from 'react-native-chart-kit';
import { launchImageLibrary } from 'react-native-image-picker';
// Icons ke liye simple text use kar rahe hain taake setup easy rahe

const screenWidth = Dimensions.get("window").width;

// --- UTILITIES (HELPERS) ---
const saveData = async (key, value) => {
  try {
    const jsonValue = JSON.stringify(value);
    await AsyncStorage.setItem(key, jsonValue);
  } catch (e) { console.error("Saving Error", e); }
};

const loadData = async (key) => {
  try {
    const jsonValue = await AsyncStorage.getItem(key);
    return jsonValue != null ? JSON.parse(jsonValue) : null;
  } catch (e) { return null; }
};

// --- SCREEN 1: FINANCE MANAGER ---
function FinanceScreen() {
  const [transactions, setTransactions] = useState([]);
  const [modalVisible, setModalVisible] = useState(false);
  const [amount, setAmount] = useState('');
  const [desc, setDesc] = useState('');
  const [type, setType] = useState('Income'); // Income or Expense

  // Load Data on Startup
  useEffect(() => {
    loadData('transactions').then(data => {
      if (data) setTransactions(data);
    });
  }, []);

  // Add Transaction Logic
  const addTransaction = () => {
    if (!amount || !desc) return alert("Please fill details");
    
    const newTxn = {
      id: Date.now().toString(),
      amount: parseFloat(amount),
      desc,
      type,
      date: new Date().toLocaleDateString()
    };

    const updatedList = [newTxn, ...transactions];
    setTransactions(updatedList);
    saveData('transactions', updatedList);
    
    setAmount(''); setDesc(''); setModalVisible(false);
  };

  // Calculations
  const totalIncome = transactions.filter(t => t.type === 'Income').reduce((acc, curr) => acc + curr.amount, 0);
  const totalExpense = transactions.filter(t => t.type === 'Expense').reduce((acc, curr) => acc + curr.amount, 0);
  const balance = totalIncome - totalExpense;

  // Chart Data Preparation
  const chartData = {
    labels: ["Start", ...transactions.slice(0, 4).map(t => t.date.slice(0,5)).reverse()],
    datasets: [{
      data: [0, ...transactions.slice(0, 4).map(t => t.type === 'Income' ? t.amount : -t.amount).reverse()]
    }]
  };

  return (
    <View style={styles.container}>
      <ScrollView>
        {/* Balance Card */}
        <View style={[styles.card, { backgroundColor: balance >= 0 ? '#d1fae5' : '#fee2e2' }]}>
          <Text style={styles.cardLabel}>Total Balance (Profit/Loss)</Text>
          <Text style={[styles.balanceText, { color: balance >= 0 ? 'green' : 'red' }]}>
            PKR {balance.toFixed(0)}
          </Text>
          <View style={styles.row}>
            <Text style={{color: 'green'}}>⬆ Inc: {totalIncome}</Text>
            <Text style={{color: 'red'}}>⬇ Exp: {totalExpense}</Text>
          </View>
        </View>

        {/* Graph */}
        <Text style={styles.header}>Growth Graph</Text>
        <LineChart
          data={chartData.datasets[0].data.length > 1 ? chartData : { labels: ["No Data"], datasets: [{ data: [0] }] }}
          width={screenWidth - 40}
          height={220}
          yAxisLabel="Rs"
          chartConfig={{
            backgroundColor: "#fff",
            backgroundGradientFrom: "#fff",
            backgroundGradientTo: "#fff",
            decimalPlaces: 0,
            color: (opacity = 1) => `rgba(0, 122, 255, ${opacity})`,
            labelColor: (opacity = 1) => `rgba(0, 0, 0, ${opacity})`,
          }}
          bezier
          style={{ marginVertical: 8, borderRadius: 16 }}
        />

        {/* History List */}
        <Text style={styles.header}>Recent History</Text>
        {transactions.map((item) => (
          <View key={item.id} style={styles.listItem}>
            <View>
              <Text style={styles.itemTitle}>{item.desc}</Text>
              <Text style={styles.itemDate}>{item.date}</Text>
            </View>
            <Text style={{ 
              fontWeight: 'bold', 
              color: item.type === 'Income' ? 'green' : 'red' 
            }}>
              {item.type === 'Income' ? '+' : '-'} {item.amount}
            </Text>
          </View>
        ))}
        <View style={{height: 100}} /> 
      </ScrollView>

      {/* Floating Add Button */}
      <TouchableOpacity style={styles.fab} onPress={() => setModalVisible(true)}>
        <Text style={styles.fabIcon}>+</Text>
      </TouchableOpacity>

      {/* ADD MODAL */}
      <Modal visible={modalVisible} animationType="slide" transparent={true}>
        <View style={styles.modalView}>
          <Text style={styles.modalTitle}>Add Transaction</Text>
          <TextInput placeholder="Amount (e.g. 5000)" keyboardType="numeric" style={styles.input} value={amount} onChangeText={setAmount} />
          <TextInput placeholder="Description (e.g. Rent)" style={styles.input} value={desc} onChangeText={setDesc} />
          
          <View style={styles.row}>
            <TouchableOpacity style={[styles.typeBtn, type === 'Income' && styles.activeType]} onPress={() => setType('Income')}>
              <Text style={{color: type === 'Income' ? 'white' : 'black'}}>Income</Text>
            </TouchableOpacity>
            <TouchableOpacity style={[styles.typeBtn, type === 'Expense' && styles.activeTypeExp]} onPress={() => setType('Expense')}>
              <Text style={{color: type === 'Expense' ? 'white' : 'black'}}>Expense</Text>
            </TouchableOpacity>
          </View>

          <TouchableOpacity style={styles.saveBtn} onPress={addTransaction}><Text style={{color:'white'}}>Save</Text></TouchableOpacity>
          <TouchableOpacity style={styles.cancelBtn} onPress={() => setModalVisible(false)}><Text>Cancel</Text></TouchableOpacity>
        </View>
      </Modal>
    </View>
  );
}

// --- SCREEN 2: NOTES & PICS ---
function NotesScreen() {
  const [notes, setNotes] = useState([]);
  const [noteModal, setNoteModal] = useState(false);
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [imageUri, setImageUri] = useState(null);

  useEffect(() => {
    loadData('notes').then(data => { if (data) setNotes(data); });
  }, []);

  const pickImage = async () => {
    const result = await launchImageLibrary({ mediaType: 'photo' });
    if (result.assets) {
      setImageUri(result.assets[0].uri);
    }
  };

  const addNote = () => {
    if (!title) return alert("Title required");
    const newNote = { id: Date.now().toString(), title, content, image: imageUri, date: new Date().toLocaleDateString() };
    const updatedNotes = [newNote, ...notes];
    setNotes(updatedNotes);
    saveData('notes', updatedNotes);
    setTitle(''); setContent(''); setImageUri(null); setNoteModal(false);
  };

  return (
    <View style={styles.container}>
      <FlatList
        data={notes}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <View style={styles.noteCard}>
            {item.image && <Image source={{ uri: item.image }} style={styles.noteImage} />}
            <Text style={styles.noteTitle}>{item.title}</Text>
            <Text>{item.content}</Text>
            <Text style={styles.itemDate}>{item.date}</Text>
          </View>
        )}
      />
      
      <TouchableOpacity style={styles.fab} onPress={() => setNoteModal(true)}>
        <Text style={styles.fabIcon}>✎</Text>
      </TouchableOpacity>

      {/* NOTE MODAL */}
      <Modal visible={noteModal} animationType="slide" transparent={true}>
        <View style={styles.modalView}>
          <Text style={styles.modalTitle}>New Note</Text>
          <TextInput placeholder="Title" style={styles.input} value={title} onChangeText={setTitle} />
          <TextInput placeholder="Details..." style={[styles.input, {height: 80}]} multiline value={content} onChangeText={setContent} />
          
          <TouchableOpacity onPress={pickImage} style={styles.attachBtn}>
            <Text>📎 Attach Image {imageUri ? '✅' : ''}</Text>
          </TouchableOpacity>

          <TouchableOpacity style={styles.saveBtn} onPress={addNote}><Text style={{color:'white'}}>Save Note</Text></TouchableOpacity>
          <TouchableOpacity style={styles.cancelBtn} onPress={() => setNoteModal(false)}><Text>Cancel</Text></TouchableOpacity>
        </View>
      </Modal>
    </View>
  );
}

// --- MAIN NAVIGATION ---
const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator
        screenOptions={{
          headerStyle: { backgroundColor: '#007AFF' },
          headerTintColor: '#fff',
          tabBarActiveTintColor: '#007AFF',
        }}>
        <Tab.Screen name="Finance & Profit" component={FinanceScreen} />
        <Tab.Screen name="Smart Notes" component={NotesScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}

// --- STYLES ---
const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f5f5f5', padding: 15 },
  card: { padding: 20, borderRadius: 15, marginBottom: 20, elevation: 4 },
  cardLabel: { fontSize: 14, color: '#555' },
  balanceText: { fontSize: 30, fontWeight: 'bold', marginVertical: 5 },
  row: { flexDirection: 'row', justifyContent: 'space-between', marginTop: 5 },
  header: { fontSize: 18, fontWeight: 'bold', marginVertical: 10, color: '#333' },
  listItem: { flexDirection: 'row', justifyContent: 'space-between', padding: 15, backgroundColor: 'white', borderRadius: 10, marginBottom: 8 },
  itemTitle: { fontSize: 16, fontWeight: '600' },
  itemDate: { fontSize: 12, color: '#999' },
  fab: { position: 'absolute', bottom: 20, right: 20, width: 60, height: 60, borderRadius: 30, backgroundColor: '#007AFF', justifyContent: 'center', alignItems: 'center', elevation: 5 },
  fabIcon: { fontSize: 30, color: 'white', fontWeight: 'bold' },
  
  // Modal Styles
  modalView: { flex: 1, backgroundColor: 'white', marginTop: 100, borderTopLeftRadius: 20, borderTopRightRadius: 20, padding: 20, shadowColor: "#000", elevation: 5 },
  modalTitle: { fontSize: 22, fontWeight: 'bold', marginBottom: 20, textAlign: 'center' },
  input: { borderWidth: 1, borderColor: '#ddd', padding: 12, borderRadius: 8, marginBottom: 15, fontSize: 16 },
  typeBtn: { padding: 10, borderWidth: 1, borderColor: '#ddd', borderRadius: 8, width: '45%', alignItems: 'center' },
  activeType: { backgroundColor: 'green', borderColor: 'green' },
  activeTypeExp: { backgroundColor: 'red', borderColor: 'red' },
  saveBtn: { backgroundColor: '#007AFF', padding: 15, borderRadius: 8, alignItems: 'center', marginTop: 10 },
  cancelBtn: { padding: 15, alignItems: 'center', marginTop: 5 },
  
  // Note Styles
  noteCard: { backgroundColor: 'white', padding: 15, borderRadius: 10, marginBottom: 10 },
  noteTitle: { fontSize: 18, fontWeight: 'bold', marginBottom: 5 },
  noteImage: { width: '100%', height: 150, borderRadius: 8, marginBottom: 10 },
  attachBtn: { padding: 15, backgroundColor: '#eee', borderRadius: 8, marginBottom: 15, alignItems: 'center' }
});