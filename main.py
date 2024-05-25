from test_speech import Text_speech
from keyboard_access import *
from browser_access import *
from commanline_access import *
from gamini_Ai import get_ai_response
import threading
from listner import Listern

obj_tts = Text_speech()
ready_for_task = False
list_extra_cmd ={
    "take a selfie" : "camera",
    "record a video" : "camera",
    "record voice" : "recorder",
    "record my screen" : "winG",
    "take notes" : "writer",
    "take screenshot": "printscreen",
    "initiate my workspace" : "workspace",
    "set my workspace": "workspace",
    "open workspace" : "workspace",
    "clear screen" : "winD",
    "switch window" : "winTab",
    "send email": "mailto"
}


def command_executor(command:str):
    global ready_for_task
    command = command.lower()

    # make sleep the personal assistant
    if any(word in command for word in ("thanks", "thank you", "done", "okay","go to sleep","error:")) and ready_for_task:
        ready_for_task = False
        obj_tts.say("Call me..! When you need somthing.! I'm going to sleep mode..!")
        return "sleeping..."
    
    if "ok window" in command and ready_for_task:
        obj_tts.say("I'm Already listening you..! ask what you want.?")
        return "ready for task"
    
    # wake up the personal assistant
    if "window" in command and not ready_for_task:
        obj_tts.say("Yes, How can I help you?")
        ready_for_task = True
        return "ready for task"
    
    # basic commands
    if ready_for_task:
        # open app present in windows.!
        if "open" in command:
            app_name = command.split("open",1)[1]  #  --> "open notepad" >> "notepad"
            if app_name != "open":
                obj_tts.say("Opening " + app_name + "...")
                t_open_app = threading.Thread(target=open_app, args=(app_name,))
                t_open_app.start()
                t_open_app.join()
                return "Task completed"
            
        # resize the window
        if any(word in command for word in ("size", "resize","full screen")):
            if "maximize" in command or "max" in command or "full screen" in command:
                obj_tts.say(app_size("max"))
                        
            elif "minimize" in command or "min" in command:
                obj_tts.say(app_size("min"))
                
            return "Resizing the window..."

        # search on google
        if "search" in command or 'find' in command:
            if "search" in command:
                query = command.split(" ")
                query.remove("search")
                query = " ".join(query)
            elif "find" in command:
                query = command.split(" ")
                query.remove("find")
                query = " ".join(query)

            obj_tts.say("Searching for " + query + "...")
            t_search = threading.Thread(target=google_search,args=(query,))
            t_search.start()
            t_search.join()
            return "Search completed"
        
        # play music or video
        if "play" in command:
            query = command.split("play").pop()
            if "music" in query or "song" in query:
                obj_tts.say("Playing " + query + "...")
                t_play = threading.Thread(target=spotify_search)
                t_play.start()
                t_play.join()
                return "Task completed"
                    
            if "video" in query:
                obj_tts.say("Which one..?")
                query = Listern().listen()
                t_play = threading.Thread(target=youtube_search,args=(query,))
                t_play.start()
                t_play.join()
                return "Task completed"

        # close the personal assistant.!
        if any(word in command for word in ("terminate", "quit","exit","bye-bye","bye")):
            obj_tts.say("Goodbye, Have a nice day!")
            exit()

        # close the app
        if "close" in command:
            obj_tts.say(close_app())
            return "Task completed"
        
        # extra commands
        if command in list_extra_cmd.keys():
            obj_tts.say("Sure, I will do .. !")
            if list_extra_cmd[command] == "camera":
                obj_tts.say("Opening " + "camera" + "...")
                t_open_app = threading.Thread(target=open_app, args=("camera",))
                t_open_app.start()
                t_open_app.join()
                return "Task completed"
                
            elif list_extra_cmd[command] == "recorder":
                obj_tts.say("Opening " + "recorder" + "...")
                t_open_app = threading.Thread(target=open_app, args=("recorder",))
                t_open_app.start()
                t_open_app.join()
                return "Task completed"
                
            elif list_extra_cmd[command] == "winG":
                obj_tts.say("Start " + "recording" + "...")
                t_open_app = threading.Thread(target=press, args=("winG",))
                t_open_app.start()
                t_open_app.join()
                return "Task completed"

            elif list_extra_cmd[command] == "winD":
                obj_tts.say("Clearing Desktop Screen "+ "...")
                t_open_app = threading.Thread(target=press, args=("winD",))
                t_open_app.start()
                t_open_app.join()
                return "Task completed"
            
            elif list_extra_cmd[command] == "winTab":
                obj_tts.say("Switching window " + "...")
                t_open_app = threading.Thread(target=press, args=("winTab",))
                t_open_app.start()
                t_open_app.join()
                return "Task completed"
                    
            elif list_extra_cmd[command] == "printscreen":
                obj_tts.say("Taking " + "screenshot" + "...")
                t_open_app = threading.Thread(target=press, args=("prtsc",))
                t_open_app.start()
                t_open_app.join()
                return "Task completed"
            
            elif list_extra_cmd[command] == "workspace":
                obj_tts.say("Initiating your " + "workspace" + "...")
                t_open_vscode = threading.Thread(target=open_app, args=("vscode",))
                t_open_app = threading.Thread(target=google_search, args=("https://github.com/DevvMaurya",))
                t_open_vscode.start()
                t_open_app.start()
                t_open_vscode.join()
                t_open_app.join()
                return "Task completed"

            elif list_extra_cmd[command] == "writer":
                obj_tts.say("Taking Notes. " + " Opening notepad" + "...")
                t_open_app = threading.Thread(target=open_app, args=("notepad",))
                t_open_app.start()
                obj_tts.say("speak what you want to write..!")
                text = Listern().listen()
                while not "Error" in text and "ok done writing" not in text:
                    t_write = threading.Thread(target=write_text, args=(text,))
                    t_write.start()
                    t_open_app.join()
                    t_write.join()
                    text = Listern().listen()
                else:
                    obj_tts.say("Check And Save your notes..!")
                    # press("altf4")

            elif list_extra_cmd[command] == "mailto":
                obj_tts.say("Opening " + "Outlook Mail" + "...")
                run_command("start mailto:")
                                
                return "Task completed"
        else :
            obj_tts.say(get_ai_response(command))
            return "Task completed"
        
        
if __name__ == "__main__":
    while True:
        command = Listern().listen()
        print("you said .. :", command)
        command_executor(command)
        # time.sleep(3)

