import pyautogui
import time
import pandas

#!!!!ATENÇÃO!!!! Para partar o codigo: colocar o cursor do mouse no extremo canto superior esquerdo
#pyautogui.press("")
#pyautogui.click("")
#pyautogui.write("")
#pyautogui.hotkey("","")

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#https://dlp.hashtagtreinamentos.com/python/intensivao/login

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#dar tempo para o site carregar 
time.sleep(5)

pyautogui.click(x=710, y=472)
pyautogui.write("viniciussiva82822@gmail.com")
pyautogui.press("tab")
pyautogui.write("qualquercoisa123")
pyautogui.press("tab")
pyautogui.press("enter")

tabela = pandas.read_csv("produtos.csv")
                         


for linha in tabela.index:
    pyautogui.click(x=719, y=323)
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    #str para pegar numeros e transformalos em strings

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    if not pandas.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)