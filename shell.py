from cmd import Cmd
import os


class shell(Cmd):
    intro = "5P34R shell"
    prompt = '(shell) => '
                           

    def default(self, arg):
        if arg in ['quit', 'q', 'close', 'exit']:
            self.close()
        else:
            print(os.system(arg)) 
        
        
    def close(self):    
        print("Exiting...")
        exit()

s = shell()
s.cmdloop()
