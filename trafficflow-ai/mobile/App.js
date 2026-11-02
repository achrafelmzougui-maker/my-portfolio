import React, { useState } from 'react';
import { ActivityIndicator, SafeAreaView, ScrollView, StatusBar, StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';

const ZONES = ['Centre-ville', 'Maâmora', 'Bir Rami', 'Mimosas'];
const COLORS = { bg: '#071320', panel: '#101f30', mint: '#64e1c7', text: '#eaf7f8', muted: '#9caec1', line: '#284052' };
const API_URL = ''; // Configure a deployed HTTPS API endpoint here. Empty = demo mode.

// Synthetic scenario only. NOT a trained model or live traffic data.
function simulate(hour, zone, weekend) {
  const morning = Math.exp(-Math.pow((hour - 8) / 2.1, 2)) * 43;
  const evening = Math.exp(-Math.pow((hour - 18) / 2.6, 2)) * 46;
  const offset = { 'Centre-ville': 14, 'Maâmora': 5, 'Bir Rami': 10, 'Mimosas': 7 }[zone] || 0;
  return Math.max(5, Math.min(98, Math.round((18 + morning + evening + offset) * (weekend ? .64 : 1))));
}
const getLevel = score => score >= 68 ? 'Élevé' : score >= 40 ? 'Moyen' : 'Faible';

export default function App() {
  const [zone, setZone] = useState(ZONES[0]);
  const [hour, setHour] = useState('08');
  const [weekend, setWeekend] = useState(false);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');
  const [mode, setMode] = useState('simulation');
  async function predict() {
    const parsedHour = Number(hour);
    if (!/^\d{1,2}$/.test(hour) || parsedHour < 0 || parsedHour > 23) {
      setError('Saisissez une heure valide entre 0 et 23.');
      return;
    }
    setError('');
    setLoading(true);
    try {
      if (!API_URL) {
        setResult(simulate(parsedHour, zone, weekend));
        setMode('simulation');
      } else {
        const controller = new AbortController();
        const timeout = setTimeout(() => controller.abort(), 8000);
        try {
          const response = await fetch(API_URL.replace(/\/$/, '') + '/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ zone, hour: parsedHour, day_of_week: weekend ? 5 : 0 }),
            signal: controller.signal
          });
          if (!response.ok) throw new Error('API indisponible (' + response.status + ')');
          const data = await response.json();
          if (typeof data.congestion_index !== 'number') throw new Error('Réponse API invalide.');
          setResult(data.congestion_index);
          setMode('api');
        } finally {
          clearTimeout(timeout);
        }
      }
    } catch (e) {
      setError(e.message || 'Erreur réseau');
      setResult(null); // Never silently present simulation as AI prediction.
    } finally {
      setLoading(false);
    }
  }
  return <SafeAreaView style={styles.root}><StatusBar barStyle="light-content" /><ScrollView contentContainerStyle={styles.content}>
    <View style={styles.header}><Text style={styles.logo}>◉ Traffic<Text style={styles.accent}>Flow</Text> AI</Text><Text style={styles.city}>KÉNITRA · MAROC</Text></View>
    <Text style={styles.eyebrow}>SMART CITY / MOBILE PROTOTYPE</Text>
    <Text style={styles.title}>Anticiper le trafic.{"\n"}<Text style={styles.accent}>Mieux se déplacer.</Text></Text>
    <Text style={styles.description}>Explorez un scénario de congestion par zone et par heure. Cette version ne fournit pas de trafic en direct.</Text>
    <View style={styles.card}><Text style={styles.heading}>Zone de Kénitra</Text><View style={styles.chips}>{ZONES.map(item => <TouchableOpacity accessibilityRole="button" accessibilityLabel={'Choisir '+item} key={item} onPress={() => {setZone(item);setResult(null);}} style={[styles.chip, zone===item && styles.chipActive]}><Text style={[styles.chipText,zone===item&&styles.chipTextActive]}>{item}</Text></TouchableOpacity>)}</View>
      <Text style={styles.heading}>Heure de départ (0–23)</Text><TextInput accessibilityLabel="Heure de départ" style={styles.input} keyboardType="number-pad" maxLength={2} value={hour} onChangeText={setHour} placeholder="08" placeholderTextColor={COLORS.muted}/>
      <Text style={styles.heading}>Type de journée</Text><View style={styles.chips}>{[[false,'Jour ouvrable'],[true,'Week-end']].map(([value,label])=><TouchableOpacity key={label} accessibilityRole="button" onPress={()=>{setWeekend(value);setResult(null);}} style={[styles.chip,weekend===value&&styles.chipActive]}><Text style={[styles.chipText,weekend===value&&styles.chipTextActive]}>{label}</Text></TouchableOpacity>)}</View>
      <TouchableOpacity accessibilityRole="button" onPress={predict} disabled={loading} style={styles.button}>{loading?<ActivityIndicator color={COLORS.bg}/>:<Text style={styles.buttonText}>Simuler la congestion →</Text>}</TouchableOpacity>
      {!!error && <Text accessibilityRole="alert" style={styles.error}>{error}</Text>}
    </View>
    {result !== null && <View style={styles.result}><Text style={styles.eyebrow}>{mode==='simulation'?'SCÉNARIO SYNTHÉTIQUE':'RÉSULTAT MODÈLE EXPÉRIMENTAL'}</Text><Text style={styles.score}>{Math.round(result)}<Text style={styles.outOf}> / 100</Text></Text><Text style={styles.level}>{getLevel(result)}</Text><Text style={styles.description}>Zone : {zone} · {hour.padStart(2,'0')}:00</Text></View>}
    <View style={styles.note}><Text style={styles.noteTitle}>TRANSPARENCE DES DONNÉES</Text><Text style={styles.description}>Mode actuel : {API_URL?'API expérimentale':'simulation locale'}. Sans données de trafic réelles ni modèle entraîné, les chiffres sont purement illustratifs. Ne pas utiliser pour des décisions de navigation.</Text></View>
    <Text style={styles.footer}>TrafficFlow AI · Projet académique · Android / iOS</Text>
  </ScrollView></SafeAreaView>;
}
const styles=StyleSheet.create({
 root:{flex:1,backgroundColor:COLORS.bg},content:{padding:22,paddingBottom:50},header:{flexDirection:'row',justifyContent:'space-between',alignItems:'center',marginBottom:44,flexWrap:'wrap',gap:8},logo:{color:COLORS.text,fontSize:20,fontWeight:'800'},accent:{color:COLORS.mint},city:{color:COLORS.muted,fontSize:10,letterSpacing:1},eyebrow:{color:COLORS.mint,fontSize:11,letterSpacing:1.5,fontWeight:'700'},title:{color:COLORS.text,fontSize:36,fontWeight:'800',lineHeight:43,letterSpacing:-1.5,marginTop:12},description:{color:COLORS.muted,fontSize:14,lineHeight:23,marginTop:12},card:{backgroundColor:COLORS.panel,borderColor:COLORS.line,borderWidth:1,borderRadius:22,padding:20,marginTop:28},heading:{color:COLORS.text,fontSize:14,fontWeight:'700',marginBottom:12,marginTop:16},chips:{flexDirection:'row',flexWrap:'wrap',gap:8},chip:{borderWidth:1,borderColor:COLORS.line,borderRadius:25,paddingHorizontal:13,paddingVertical:11},chipActive:{backgroundColor:COLORS.mint,borderColor:COLORS.mint},chipText:{color:COLORS.text,fontSize:12},chipTextActive:{color:COLORS.bg,fontWeight:'800'},input:{borderWidth:1,borderColor:COLORS.line,borderRadius:12,color:COLORS.text,padding:14,fontSize:17},button:{backgroundColor:COLORS.mint,padding:17,borderRadius:12,alignItems:'center',marginTop:25},buttonText:{color:COLORS.bg,fontWeight:'800'},error:{color:'#ff9999',marginTop:12},result:{backgroundColor:'#14343c',borderWidth:1,borderColor:'#2e706e',borderRadius:22,padding:24,marginTop:18},score:{fontSize:62,fontWeight:'900',color:COLORS.mint,marginTop:10},outOf:{fontSize:17,color:COLORS.muted},level:{fontSize:20,fontWeight:'700',color:COLORS.text},note:{marginTop:20,padding:18,borderRadius:18,borderWidth:1,borderColor:COLORS.line},noteTitle:{color:COLORS.mint,fontSize:11,letterSpacing:1.5,fontWeight:'700'},footer:{color:COLORS.muted,textAlign:'center',fontSize:11,marginTop:28}
});
