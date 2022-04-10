import random
import string

WORDLIST_FILENAME = "kelimeler.txt"


def load_words():
   
    
  
    inFile = open(WORDLIST_FILENAME, 'r')    
    line = inFile.readline()   
    wordlist = line.split()
  
    return wordlist



def choose_word(wordlist):
   
    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    
 for i in secret_word:   
    if i in letters_guessed:      
        return True
 return False    
        





def get_guessed_word(secret_word, letters_guessed):
    
    harfler = ""
    for harf in secret_word:   
       if harf  in letters_guessed:      
            harfler += harf + ' '
       else : 
           harfler = harfler + '_ ' 
    return harfler        
   

def cumle(secret_word,letters_guessed) :
    
        
        harfler = ""
        for harf in secret_word:   
           if harf  in letters_guessed:      
                harfler += harf 
           
               
        return harfler  
    

def get_available_letters(letters_guessed):
    
    ingHarf = "abcdefghijklmnopqrstuvwxyz"
    kalanHarfler = ""
    for ing in ingHarf : 
        if ing not in letters_guessed :
            kalanHarfler = ing+ kalanHarfler  
        
    return kalanHarfler


def adamAsmaca(secret_word):
    uyarı = 3 
    unluler = ['a','e','i','o','u']
    
    print("Adam asmaca oyununa hoş geldiniz") 
    kelimeUzunlugu = str(len(secret_word))
    print("Bulmanız gereken kelime ", kelimeUzunlugu ," harf içerir.")
    kalanTahmin = 6 
    tahminEdilenHarfler = []
    dogruTahmin = []
   
    while kalanTahmin > 0 : 
            print("Kalan tahmin hakkın : " , kalanTahmin)
       
  
            print(get_guessed_word(secret_word,dogruTahmin))    
            harfTahmini = str.lower(input('Tahmin için harf giriniz :'))
        
            
            
            
            
        
            
            if(harfTahmini  in tahminEdilenHarfler ) : 
                print("Bu harfi zaten yazdın")
                if(uyarı == 3) :
                    
                    uyarı = uyarı - 1 
                if(uyarı < 3 and uyarı != 0) : 
                    print(uyarı , " hakkınız bulunmaktadır . lütfen Dikkatli olun")
                    uyarı = uyarı - 1 
                if(uyarı == 0) :
                    kalanTahmin = kalanTahmin - 1 
                    
                    print("Uyarı hakkınız kalmadığı için tahmin hakkınız azalmıştır.",
                          "kalan tahmin : " 
                           , kalanTahmin)
            else : 
                
                if (str.isalpha(harfTahmini) == True):
                    
                    tahminEdilenHarfler.append(harfTahmini) 
                    if(harfTahmini in secret_word) : 
                       
                               
                       
                        dogruTahmin.append(harfTahmini)
                        a = cumle(secret_word,dogruTahmin)
                        if(a == secret_word) :
                            print("Tebrikler Oyunu kazandınız : ")
                            break
                    
                    else : 
                        if(harfTahmini in unluler) :
                           kalanTahmin = kalanTahmin - 1
                             
                                 
                           kalanTahmin = kalanTahmin - 1
                            
                        else : 
                            
                            kalanTahmin = kalanTahmin - 1 
                                  
                        print("Yanlış tahmin ")
                elif(harfTahmini == '*') :
                    print(str(show_possible_matches(get_guessed_word(secret_word,tahminEdilenHarfler))))
                else : 
                    print( "Lütfen geçerli bir harf giriniz")
                    if(uyarı == 3) :
                        
                        uyarı = uyarı - 1 
                    elif(uyarı < 3 and uyarı != 0) : 
                        print(uyarı , " hakkınız bulunmaktadır . lütfen Dikkatli olun")
                        uyarı = uyarı - 1 
                    elif(uyarı == 0) :
                        kalanTahmin = kalanTahmin - 1 
                        
                        print("Uyarı hakkınız kalmadığı için tahmin hakkınız azalmıştır.",
                              "kalan tahmin : " 
                               , kalanTahmin)
       
           
            print("Kalan Harfler : ", get_available_letters(tahminEdilenHarfler))
    if(kalanTahmin == 0 ) :
        print("Üzgünüm, tahminleriniz tükendi. Kelime başkaydı."+ "\n"+"Kelime : " ,secret_word)
   



def match_with_gaps(my_word, other_word):
    
    my_word = my_word.replace(' ','')
    other_word = other_word.replace(' ','')
    esles = False
    i=0
    if len(my_word)==len(other_word):
        while i<len(my_word):
            if (my_word[i] in other_word[i]):
                esles = True
            elif (my_word[i] not in other_word[i]) and (my_word[i]=='_'):
                esles = True
            else:
                return False
            i = i + 1 
    return esles
  


def show_possible_matches(my_word):
    
  my_word = my_word.replace(' ','')
  sonuc = []
  j=0
  while j<len(wordlist):
       if (len(my_word)== len(wordlist[j])):
           if (match_with_gaps(my_word,wordlist[j])==True): 
               sonuc.append(wordlist[j])
       j+=1
  if len(sonuc) == 0:
       sonuc = ' Bulunamadı.. '
  return sonuc
  



    



if __name__ == "__main__":
  
    secret_word = choose_word(wordlist)
    adamAsmaca(secret_word)
    
  
        

