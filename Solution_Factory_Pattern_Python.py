# Solution using the   
# factory design pattern  
  
class French_Language:   
  
   #it will return the french version  
  
   def __init__(self):   
  
      self.translations = {"book": "voiture", "phone": "biclothtte",   
                     "cloth":"clothtte"}   
  
   def localize(self, message):   
  
      """change the message using translations"""  
      return self.translations.get(msg, msg)   
  
class Spanish_Language:   
   #it will return the spanish version  
  
   def __init__(self):   
      self.translations = {"book": "libro", "phone": "teléfono",  
                     "cloth":"paño"} 
   def localize(self, msg):   
  
      #change the message using translations  
      return self.translations.get(msg, msg)   
  
class English_Language:   
   """Simply return the same message"""  
  
   def localize(self, msg):   
      return msg   
  
def Factory(language ="English"):   
  
   """Factory Method"""  
   localizers = {   
      "French": French_Language,   
      "English": English_Language,   
      "Spanish": Spanish_Language,   
   }   
  
   return localizers[language]()   
  
if __name__ == "__main__":   
  
   fr = Factory("French")   
   en = Factory("English")   
   sp = Factory("Spanish")   
  
   message = ["book", "phone", "cloth"]   
  
   for m in message:   
      print(fr.localize(m))   
      print(en.localize(m))   
      print(sp.localize(m))   