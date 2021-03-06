# python

import lx, lifesaver


class ResetPrefsCommandClass(lifesaver.CommanderClass):

    def commander_execute(self, msg, flags):
        
        clearCmd = 'lifesaver.clearPrefs'
        for i in lifesaver.KEEPERS:
            clearCmd += " " + str(lx.eval('lifesaver.preference %s ?' % i[3]))
        
        lx.eval(clearCmd)
      
                
lx.bless(ResetPrefsCommandClass, 'lifesaver.resetPrefs')