import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import smtplib

# Inicializando o mecanismo Text-to-Speech
engine = pyttsx3.init()

def speak(text):
    """Função para o assistente falar."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Função para o assistente ouvir o comando de voz."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ouvindo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Reconhecendo...")
        command = recognizer.recognize_google(audio, language="pt-BR").lower()
        print("Comando: " + command)
        return command
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
        return ""
    except sr.RequestError as e:
        print(f"Erro no serviço de reconhecimento de voz; {e}")
        return ""

def send_email():
    # Configurar informações de e-mail
    email_address = "seu_email@gmail.com"
    email_password = "sua_senha"
    recipient_email = "destinatario@example.com"
    subject = "Assunto do E-mail"
    body = "Corpo do E-mail"

    try:
        # Configurar o servidor SMTP do Gmail
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_address, email_password)

        # Criar e enviar o e-mail
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(email_address, recipient_email, message)

        speak("E-mail enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        speak("Desculpe, ocorreu um erro ao enviar o e-mail.")

    finally:
        # Encerrar a conexão com o servidor SMTP
        server.quit()

def open_photo():
    # Substitua "caminho/para/suas/fotos" pelo caminho real para suas fotos
    photo_directory = "caminho/para/suas/fotos"

    try:
        # Listar arquivos de imagem no diretório
        photos = [f for f in os.listdir(photo_directory) if f.endswith(('.jpg', '.jpeg', '.png'))]

        if not photos:
            speak("Não foi possível encontrar fotos.")
        else:
            # Escolher a primeira foto na lista
            photo_path = os.path.join(photo_directory, photos[0])
            os.system(f"start {photo_path}")  # Abrir a foto com o visualizador de fotos padrão

    except Exception as e:
        print(f"Erro ao abrir foto: {e}")
        speak("Desculpe, ocorreu um erro ao abrir a foto.")

def play_music():
    # Substitua "caminho/para/suas/musicas" pelo caminho real para suas músicas
    music_directory = "caminho/para/suas/musicas"

    try:
        # Listar arquivos de áudio no diretório
        music_files = [f for f in os.listdir(music_directory) if f.endswith(('.mp3', '.wav'))]

        if not music_files:
            speak("Não foi possível encontrar músicas.")
        else:
            # Escolher a primeira música na lista
            music_path = os.path.join(music_directory, music_files[0])
            os.system(f"start {music_path}")  # Abrir a música com o player de música padrão

    except Exception as e:
        print(f"Erro ao reproduzir música: {e}")
        speak("Desculpe, ocorreu um erro ao reproduzir a música.")

def open_browser():
    speak("Qual site você gostaria de abrir?")
    website = listen()

    if website:
        webbrowser.open(f"https://www.{website}.com")
        speak(f"Abrindo o site {website}.")

def main():
    speak("Olá! Como posso ajudar você hoje?")

    while True:
        command = listen()

        if "email" in command:
            speak("Enviando e-mail.")
            send_email()
        elif "foto" in command:
            speak("Abrindo a galeria de fotos.")
            open_photo()
        elif "música" in command:
            speak("Reproduzindo música.")
            play_music()
        elif "navegador" in command:
            speak("Abrindo o navegador.")
            open_browser()
        elif "sair" in command or "parar" in command:
            speak("Até logo!")
            break
        else:
            speak("Desculpe, não entendi o comando.")

if __name__ == "__main__":
    main()
