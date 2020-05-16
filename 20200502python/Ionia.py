from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

champs = {
  "ch1": {
      "id" : "ch1",
      "name": "Akali", 
      "intro": "Abandoning the Kinkou Order and her title of the Fist of Shadow, Akali now strikes alone, ready to be the deadly weapon her people need. Though she holds onto all she learned from her master Shen, she has pledged to defend Ionia from its enemies, one kill at a time.",
      "src": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Akali_0.jpg" },
  "ch2": {  
      "id" : "ch2",
      "name": "Shen", 
      "intro": "Among the secretive, Ionian warriors known as the Kinkou, Shen serves as their leader, the Eye of Twilight. He longs to remain free from the confusion of emotion, prejudice, and ego, and walks the unseen path of dispassionate judgment between the spirit.",
      "src": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Shen_0.jpg" },
  "ch3": {  
      "id" : "ch3",
      "name": "Yasuo", 
      "intro": "An Ionian of deep resolve, Yasuo is an agile swordsman who wields the air itself against his enemies. As a proud young man, he was falsely accused of murdering his master—unable to prove his innocence, he was forced to slay his own brother in self defense.",
      "src": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Yasuo_0.jpg" },
  "ch4": { 
      "id" : "ch4",
      "name": "Zed", 
      "intro": "Utterly ruthless and without mercy, Zed is the leader of the Order of Shadow, an organization he created with the intent of militarizing Ionia's magical and martial traditions to drive out Noxian invaders. During the war, desperation led him to unlock the secret shadow form—a malevolent spirit magic as dangerous and corrupting as it is powerful.",
      "src": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Zed_0.jpg" },
  "ch5": {  
      "id" : "ch5",
      "name": "Master Yi", 
      "intro": "Master Yi has tempered his body and sharpened his mind, so that thought and action have become almost as one. Though he chooses to enter into violence only as a last resort, the grace and speed of his blade ensures resolution is always swift. As one of the last living practitioners of the Ionian art of Wuju, Yi has devoted his life to continuing the legacy of his people.",
      "src": "https://cdn1.dotesports.com/wp-content/uploads/2019/02/25141611/MasterYi_0.jpg" },
  "ch6": {  
      "id" : "ch6",
      "name": "Irelia", 
      "intro": "The Noxian occupation of Ionia produced many heroes, none more unlikely than young Irelia of Navori. Trained in the ancient dances of her province, she adapted her art for war, using the graceful and carefully practised movements to levitate a host of deadly blades.",
      "src": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Irelia_0.jpg" }

}

@app.route('/')
def school():
    return render_template('school.html', champs = champs)

@app.route('/champ/<chid>')
def champ(chid):
    abis = champs[chid]
    return render_template('abi.html', abi = abis)