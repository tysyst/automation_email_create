def ムームードメインのアカウントへログイン(): #📍 日本語 !?
    print("メアド作成スタート")
    time.sleep(1)
    pyautogui.hotkey('right')
    time.sleep(1)
    pyautogui.hotkey('ctrl','shift','alt',':') #メアド作成日時入力
    time.sleep(0.5)
    pyautogui.hotkey('right') #ドメイン番号列まで移動
    time.sleep(1)
    pyautogui.hotkey('right')
    time.sleep(1)
    pyautogui.hotkey('ctrl','c') #ドメイン番号コピー
    time.sleep(2)
    domain_number = pyperclip.paste() #ドメイン番号を変数に代入
    # print(copy)
    webbrowser.open("https://muumuu-domain.com/?mode=conpane&state=mail_edit_address") #muumuu-domain開く
    time.sleep(3)

    #📍ここに１行とか、空白行があっても見やすくて良いのではないでしょうか
    #ログイン時のアカウント名入力欄移動後、既存の情報を消す
    for i in range(3):
        pyautogui.hotkey('tab')
        time.sleep(0.2) 
    pyautogui.hotkey('backspace') 

    #ドメイン番号でアカウント切り替え
    #📍３つのアカウントで分岐が違うなら、それぞれの動きについて、共通の関数を作ってもよいのでは？
    #📍 例： __login(account_name):
    if 3<= int(domain_number) <=20 : #（3～20）真之アカ
        time.sleep(0.6)
        pyperclip.copy("saneyuki.akiyama2018@gmail.com")
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.6)
        pyautogui.hotkey('tab') #パスワード入力欄へ移動
        time.sleep(0.6)
        pyautogui.hotkey('backspace') #既存のパスワード削除 
        time.sleep(0.6)
        pyperclip.copy(os.environ['pass1']) #環境変数にあるパスワード取得
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.6)
        pyautogui.hotkey('tab')
        time.sleep(0.6)
        pyautogui.hotkey('enter')  #ログインボタンクリック
        time.sleep(6)
        for i in range(14):
            pyautogui.hotkey('down')
            time.sleep(0.2)   
        pyautogui.click(x=1034, y=972) #メールアドレス作成ボタンクリック
        time.sleep(0.5)
    elif 21<= int(domain_number) <=25: #（21～25）初代アカ
        time.sleep(0.6)
        pyperclip.copy("ty_para@hotmail.com")
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.6)
        pyautogui.hotkey('tab') #パスワード入力欄へ移動
        time.sleep(0.6)
        pyautogui.hotkey('backspace') #既存のパスワード削除
        time.sleep(0.6)
        pyperclip.copy(os.environ['pass2']) #環境変数にあるパスワード取得
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.6)
        pyautogui.hotkey('tab')
        time.sleep(0.6)
        pyautogui.hotkey('enter')  #ログインボタンクリック
        time.sleep(6)
        for i in range(14):
            pyautogui.hotkey('down')
            time.sleep(0.2)   
        pyautogui.click(x=1034, y=972) #メールアドレス作成ボタンクリック
        time.sleep(0.5)
    elif 26<= int(domain_number) <= 32: #（26～32）3代目アカ
        time.sleep(0.6)
        pyperclip.copy("kita.minami.ue@gmail.com")
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.6)
        pyautogui.hotkey('tab') #パスワード入力欄へ移動
        time.sleep(0.6)
        pyautogui.hotkey('backspace')  #既存のパスワード削除
        time.sleep(0.6)
        pyperclip.copy(os.environ['pass3']) #環境変数にあるパスワード取得
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.6)
        pyautogui.hotkey('tab')
        time.sleep(0.6)
        pyautogui.hotkey('enter') #ログインボタンクリック
        time.sleep(6)
        for i in range(20):
            pyautogui.hotkey('down')
            time.sleep(0.2)   
        create = pyautogui.locateOnScreen('create.png' , confidence=0.7)
        print(create)
        pyautogui.click(create) #メールアドレス作成ボタンクリック
        # pyautogui.click(x=1034, y=972) #メールアドレス作成ボタンクリック
        time.sleep(0.5)
