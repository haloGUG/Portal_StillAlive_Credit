import shutil
import time
from playsound import playsound
import threading

mp3_path = r"D:\vcdata\workspace\草稿\still alive.mp3"

columns, rows = shutil.get_terminal_size()

column_ly = 2 
column_ph = 59

row_ly = 5
row_ph = 5

def play_mp3(mp3_path):
    # 模拟播放MP3的操作
    playsound(mp3_path)


def print_lyrics(text, row, column, delay1, delay2):
    for i, char in enumerate(text):
        # 移动光标到指定的行和列
        print(f"\033[{row};{column}H", end='')
        # 打印当前字符
        print(text[:i + 1], end='', flush=True)
        # 暂停一段时间
        time.sleep(delay1)
    time.sleep(delay2)
    
    # 移动光标回到屏幕左上角
    print("\033[H", end='')

def print_ph(ph, row, column, delay1, delay2):
    row0 = row
    lop = ph.splitlines()
    for line in lop:
        # 移动光标到指定的行和列
        print(f"\033[{row0};{column}H", end='')
        # 打印当前字符
        print(line, end='', flush=True)
        row0 = row0 + 1
        # 暂停一段时间
        time.sleep(delay1)
    time.sleep(delay2)
    
    # 移动光标回到屏幕左上角
    print("\033[H", end='')

def build_frame1():
    for i in range(2,26):
        print_lyrics('|',i,1,0,0)
    for i in range(2,56):
        print_lyrics('-',1,i,0,0)
    for i in range(2,26):
        print_lyrics('|',i,56,0,0)
    for i in range(2,56):
        print_lyrics('-',26,i,0,0)

    for i in range(59,106):
        print_lyrics('-',4,i,0,0)
    for i in range(59,106):
        print_lyrics('-',1,i,0,0)
    print_lyrics('|',2,58,0,0)
    print_lyrics('|',3,58,0,0)
    print_lyrics('|',2,106,0,0)
    print_lyrics('|',3,106,0,0)

def print_credits(credits):
    lines = credits.splitlines()
    iterator = iter(lines)
    for line1, line2 in zip(iterator, iterator):
      print(f"\033[2;60H\033[K\033[3;60H\033[K", end='')
      print_lyrics('|',2,106,0,0)
      print_lyrics('|',3,106,0,0)
      print_lyrics(line1, 2, 60, 0, 0)
      print_lyrics(line2, 3, 60, 0.08, 0.6)




def print_lyric():
    ############### Page 1 ################
    print_lyrics("This was a triumph.", row_ly, column_ly,0.15,2.1)
    print_lyrics("I'm making a note here:", row_ly + 1, column_ly,0.1,0.2)
    print_lyrics("HUGE SUCCESS.", row_ly + 2, column_ly,0.1,1.5)
    print_lyrics("It's hard to overstate", row_ly + 3, column_ly,0.1,0)
    print_lyrics("my satisfaction.", row_ly + 4, column_ly,0.1,2.2)
    print_lyrics("Aperture Science", row_ly + 5, column_ly,0.08,0)

    print_ph(ph1,row_ly,column_ph,0.002,1.5)

    print_lyrics("We do what we must", row_ly + 6, column_ly,0.2,0)
    print_lyrics("because we can.", row_ly + 7, column_ly,0.2,0.6)
    print_lyrics("For the good of all of us.", row_ly + 8, column_ly,0.1,0)

    print_ph(ph2,row_ly,column_ph,0.002,0.1)

    print_lyrics("Except the ones who are dead.", row_ly + 9, column_ly,0.06,0)
    print_lyrics("", row_ly + 10, column_ly,0,0),

    print_ph(ph1,row_ly,column_ph,0.002,0)

    print_lyrics("But there's no sense crying", row_ly + 11, column_ly,0.07,0)
    print_lyrics("over every mistake.", row_ly + 12, column_ly,0.07,0.5)
    print_lyrics("You just keep on trying", row_ly + 13, column_ly,0.07,0)
    print_lyrics("till you run out of cake.", row_ly + 14, column_ly,0.07,0)

    print_ph(ph3,row_ly,column_ph,0.002,0.5)

    print_lyrics("And the Science gets done.", row_ly + 15, column_ly,0.07,0.1)
    print_lyrics("And you make a neat gun.", row_ly + 16, column_ly,0.08,0)

    print_ph(ph1,row_ly,column_ph,0.002,0.1)

    print_lyrics("For the people who are", row_ly + 17, column_ly,0.07,0)
    print_lyrics("still alive.", row_ly + 18, column_ly,0.07,1)

    ############### Page 2 ################
    print("\033[2J",end='')
    build_frame1()
    print_ph(ph1,row_ly,column_ph,0.002,0)
    print_lyrics("Forms FORM-55551-5:", 2, column_ly,0.05,0.05),
    print_lyrics("Personnel File Addendum:", 3, column_ly,0.05,0.05),
    print_lyrics("", 4, column_ly,0,0),
    print_lyrics("Dear <<Subject Name Here>>,", 5, column_ly,0.05,2.45),

    print_lyrics("I'm not even angry.", row_ly + 2, column_ly,0.1,2.5)
    print_lyrics("I'm being so sincere right now.", row_ly + 3, column_ly,0.1,2)
    print_lyrics("Even though you broke my heart.", row_ly + 4, column_ly,0.08,0)

    print_ph(ph4,row_ly,column_ph,0.002,0.5)

    print_lyrics("And killed me.", row_ly + 5, column_ly,0.1,0.5)
    print_lyrics("And tore me to pieces.", row_ly + 6, column_ly,0.09,2)
    print_lyrics("And threw every piece into a fire.", row_ly + 7, column_ly,0.1,1.5)

    print_ph(ph6,row_ly,column_ph,0.002,2.0)

    print_lyrics("As they burned it hurt because", row_ly + 8, column_ly,0.1,0)
    print_lyrics("I was so happy for you!", row_ly + 9, column_ly,0.1,0.1)
    print_lyrics("Now these points of data", row_ly + 10, column_ly,0.1,0)
    print_lyrics("make a beautiful line.", row_ly + 11, column_ly,0.1,0)

    print_ph(ph7,row_ly,column_ph,0.002,0.1)

    print_lyrics("And we're out of beta.", row_ly + 12, column_ly,0.09,0)
    print_lyrics("We're releasing on time.", row_ly + 13, column_ly,0.08,0)

    print_ph(ph5,row_ly,column_ph,0.002,0.1)

    print_lyrics("So I'm GLaD and I got burned.", row_ly + 14, column_ly,0.07,0)

    print_ph(ph3,row_ly,column_ph,0.002,0.08)

    print_lyrics("Think of all the things we learned", row_ly + 15, column_ly,0.06,0)
    print_lyrics("For the people who are", row_ly + 16, column_ly,0.06,0)
    print_lyrics("Still alive.", row_ly + 17, column_ly,0.06,1)

    ############ Page 3 ##############
    print("\033[2J",end='')
    build_frame1()

    print_ph(ph1,row_ly,column_ph,0.002,0)

    print_lyrics("Forms FORM-55551-6:", 2, column_ly,0.05,0),
    print_lyrics("Personnel File Addendum Addendum:", 3, column_ly,0.05,0),
    print_lyrics("", 4, column_ly,0,0),
    print_lyrics("One last thing:", 5, column_ly,0.05,2.45),

    print_lyrics("Go ahead and leave me.", row_ly + 2, column_ly,0.1,2)
    print_lyrics("I think I prefer to stay in side.", row_ly + 3, column_ly,0.1,1.8)
    print_lyrics("Maybe you'll find someone else", row_ly + 4, column_ly,0.11,0)
    print_lyrics("To help you.", row_ly + 5, column_ly,0.11,1.9)
    print_lyrics("Maybe Black Mesa...", row_ly + 6, column_ly,0.09,0)

    print_ph(ph8,row_ly,column_ph,0.002,2.0)

    print_lyrics("THAT WAS A JOKE.", row_ly + 7, column_ly,0.1,0.1)
    print_lyrics("HAHA, FAT CHANCE.", row_ly + 8, column_ly,0.1,1.5)
    print_lyrics("Anyway, this cake is great.", row_ly + 9, column_ly,0.1,0)

    print_ph(ph9,row_ly,column_ph,0.002,0.1)

    print_lyrics("It's so delicious and moist.", row_ly + 10, column_ly,0.1,0)

    print_ph(ph10,row_ly,column_ph,0.002,0.2)

    print_lyrics("Look at me still talking", row_ly + 11, column_ly,0.07,0)
    print_lyrics("when there's Science to do.", row_ly + 12, column_ly,0.07,0)

    print_ph(ph2,row_ly,column_ph,0.002,0.1)

    print_lyrics("When I look out there,", row_ly + 13, column_ly,0.06,0)
    print_lyrics("it makes me GLaD I'm not you.", row_ly + 14, column_ly,0.06,0)

    print_ph(ph1,row_ly,column_ph,0.002,0.1)

    print_lyrics("I've experiments to run.", row_ly + 15, column_ly,0.09,0)

    print_ph(ph5,row_ly,column_ph,0.001,0.06)

    print_lyrics("There is research to be done.", row_ly + 16, column_ly,0.06,0)

    print_ph(ph1,row_ly,column_ph,0.001,0.06)

    print_lyrics("On the people who are", row_ly + 17, column_ly,0.08,0)
    print_lyrics("still alive.", row_ly + 18, column_ly,0.08,1)

    ############# Page 4 #############
    print("\033[2J",end='')
    build_frame1()
    print_ph(ph1,row_ly,column_ph,0.002,0)
    print_lyrics("PS: And believe me I am", row_ly, column_ly,0.09,0)
    print_lyrics("still alive.", row_ly + 1, column_ly,0.09,0.5)
    print_lyrics("PPS: I'm doing Science and I'm", row_ly + 2, column_ly,0.07,0)
    print_lyrics("still alive.", row_ly + 3, column_ly,0.07,1.0)
    print_lyrics("PPPS: I feel FANTASTIC and I'm", row_ly + 4, column_ly,0.07,0)
    print_lyrics("still alive.", row_ly + 5, column_ly,0.07,1.9)
    print_lyrics("FINAL THOUGH:", row_ly + 7, column_ly,0.01,0)
    print_lyrics("While you're dying I'll be", row_ly + 8, column_ly,0.07,0)
    print_lyrics("still alive.", row_ly + 9, column_ly,0.07,0.9)
    print_lyrics("FINAL THOUGH PS:", row_ly + 11, column_ly,0.01,0)
    print_lyrics("And when you're dead I will be", row_ly + 12, column_ly,0.07,0)
    print_lyrics("still alive.", row_ly + 13, column_ly,0.07,1.1)
    print_lyrics("STILL ALIVE", row_ly + 15, column_ly,0.07,1.1)
    print_lyrics("STILL ALIVE", row_ly + 17, column_ly,0.07,1.1)









credits = r""">LIST PERSONNEL
            
Gautam Babbar
Ted Backman
Kelly Bailey
Jeff Ballinger
Aaron Barber
Jeep Barnett
Jeremy Bennett
Dan Berger
Yahn Bernier
Ken Birdwell
Derrick BirumMike Blaszczak
Iestyn Bleasdale-Shepherd
Chris Bokitch
Steve Bond
Matt Boone
Antoine Bourdon
Jamaal Bradley
Jason Brashill
Charlie Brown
Charlie Burgin
Andrew Burke
Augusta Butlin
Julie Caldwell
Dario Casali
Chris Chin
Jess Cliffe
Phil Co
John Cook
Christen Coomer
Greg Coomer
Scott Dalton
Kerry Davis
Jason Deakins
Joe Demers
Ariel Diaz
Quintin Doroquez
Jim Dose
Chris Douglass
Laura Dubuk
Mike Dunkle
Mike Durand
Mike Dussault
Dhabih Eng
Katie Engel
Chet Faliszek
Adrian Finol
Bill Fletcher
Moby Francke
Stephane Gaudette
Kathy Gehrig
Vitaliy Genkin
Paul Graham
Chris Green
Chris Grinstead
John Guthrie
Aaron Halifax
Reagan Halifax
Leslie Hall
Jeff Hameluck
Joe Han
Don Holden
Jason Holtman
Gray Horsfield
Keith Huggins
Jim Hughes
Jon Huisingh
Brian Jacobson
Lars Jensvold
Erik Johnson
Jakob Jungels
Rich Kaethler
Steve Kalning
Aaron Kearly
Iikka Keranen
David Kircher
Eric Kirchmer
Scott Klintworth
Alden Kroll
Marc Laidlaw
Jeff Lane
Tim Larkin
Dan LeFree
Isabelle LeMay
Tom Leonard
Jeff Lind
Doug Lombardi
Bianca Loomis
Richard Lord
Realm Lovejoy
Randy Lundeen
Scott Lynch
Ido Magal
Nick Maggiore
John McCaskey
Patrick McClard
Steve McClure
Hamish McKenzie
Gary McTaggart
Jason Mitchell
Mike Morasky
John Morello II
Bryn Moslow
Arsenio Navarro
Gabe Newell
Milton Ngan
Jake Nicholson
Martin Otten
Nick Papineau
Karen Prell
Bay Raitt
Tristan Reidford
Alfred Reynolds
Matt Rhoten
Garret Rickey
Dave Riller
Elan Ruskin
Matthew Russell
Jason Ruymen
David Sawyer
Marc Scaparro
Wade Schin
Matthew Scott
Aaron Seeler
Jennifer Seeley
Taylor Sherman
Eric Smith
Jeff Sorensen
David Speyrer
Jay Stelly
Jeremy Stone
Eric Strand
Kim Swift
Kelly Thornton
Eric Twelker
Carl Uhlman
Doug Valente
Bill Van Buren
Gabe Van Engel
Alex Vlachos
Robin Walker
Joshua Weier
Andrea Wicklund
Greg Winkler
Erik Wolpaw
Doug Wood
Matt T. Wood
Danika Wright
Matt Wright
Shawn Zabecki
Torsten Zabka 
            
            
'Still Alive' by:
Jonathan Coulton
            
Voices:
Ellen McLain - GlaDOS, Turrets
Mike Patton - THE ANGER SPHERE
            
Voice Casting:
Shana Landsburg\Teri Fiddleman
            
Voice Recording:
Pure Audio, Seattle, WA
            
Voice recording
scheduling and logistics:
Pat Cockburn, Pure Audio
            
Translations:
SDL
            
Crack Legal Team:
Liam Lavery
Karl Quackenbush
Kristen Boraas
Kevin Rosenfield
Alan Bruggeman
Dennis Tessier
            
Thanks for the use of their face:
Alesia Glidewell - Chell
            
Special thanks to everyone at:
Alienware
ATI
Dell
Falcon Northwest
Havok
SOFTIMAGE
and Don Kemmis, SLK Technologies
            
            
THANK YOU FOR PARTICIPATING
IN THIS
ENRICHMENT CENTER ACTIVITY!!"""

ph1 = '''
                    .,-:;//;:=,                
                . :H@@@MM@M#H/.,+%;,           
             ,/X+ +M@@M@MM%=,-%HMMM@X/,        
           -+@MM; #M@@MH+-,;XMMMM@MMMM@+-      
          ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.    
        ,%MM@@MH ,@%=            .---=-=:=,.   
        =@#@@@MX .,              -%HX##%%%+;   
       =-./@M@M$                  .;@MMMM@MM:  
       X@/ -#MM/                    .+MM@@@M$  
      ,@M@H: :@:                    . =X#@@@@- 
      ,@@@MMX, .                    /H- ;@M@M= 
      .H@@@@M@+,                    %MM+..%#$. 
       /MMMM@MMH/.                  XM@MH; =;  
        /%+%#XHH@$=              , .H@@@@MX,   
         .=--------.           -%H.,@@@@@MX,   
         .%MM@@@HHHXX###%+= .:#MMX =M@@MM%.    
           =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=      
             =%@M@M#@$-.=#@MM@@@M; %M%=        
               ,:+$+-,/H#MMMMMMM@= =,          
                     =++%%%%+/:-.              
                     
'''
    
ph2= '''
                   =+$HM####@H%;,              
                /H###############M$,           
                ,@################+            
                 .H##############+             
                   X############/              
                    $##########/               
                     %########/                
                      /X/;;+X/                 
                       -XHHX-                  
                      ,######,                 
      #############X  .M####M.  X############# 
      ##############-   -//-   -############## 
      X##############%,      ,+##############X 
      -##############X        X##############- 
       %############%          %############%  
        %##########;            ;##########%   
         ;#######M=              =M#######;    
          .+M###@,                ,@###M+.     
             :XH.                  .HX:        
                                               
'''

ph3 = '''
                       =/;;/-                  
                      +:    //                 
                     /;      /;                
                    -X        H.               
      .//;;;:;;-,   X=        :+   .-;:=;:;%;. 
      M-       ,=;;;#:,      ,:#;;:=,       ,@ 
      :%           :%.=/++++/=.$=           %= 
       ,%;         %/:+/;,,/++:+/         ;+.  
         ,+/.    ,;@+,        ,%H;,    ,/+,    
            ;+;;/= @.  .H##X   -X :///+;       
            ;+=;;;.@,  .XM@$.  =X.//;=%/.      
         ,;:      :@%=        =$H:     .+%-    
       ,%=         %;-///==///-//         =%,  
      ;+           :%-;;;:;;;;-X-           +: 
      @-      .-;;;;M-        =M/;;;-.      -X 
       :;;::;;-.    %-        :+    ,-;;-;:==  
                    ,X        H.               
                     ;/      %=                
                      //    +;                 
                       ,////,                  

'''

ph4 = '''
                                .,---.         
                              ,/XM#MMMX;,      
                            -%##########M%,    
                           -@######%  $###@=   
            .,--,         -H#######$   $###M:  
         ,;$M###MMX;     .;##########$;HM###X= 
       ,/@##########H=      ;################+ 
      -+#############M/,      %##############+ 
      %M###############=      /##############: 
      H################      .M#############;. 
      @###############M      ,@###########M:.  
      X################,      -$=X#######@:    
      /@##################%-     +######$-     
      .;##################X     .X#####+,      
       .;H################/     -X####+.       
         ,;X##############,       .MM/         
            ,:+$H@M#######M#$-    .$$=         
                 .,-=;+$@###X:    ;/=.         
                        .,/X$;   .::,          
                            .,    ..           

'''

ph5 = '''
                  .+                           
                   /M;                         
                    H#@:              ;,       
                    -###H-          -@/        
                     %####$.  -;  .%#X         
                      M#####+;#H :M#M.         
      ..          .+/;%#########X###-          
       -/%H%+;-,    +##############/           
          .:$M###MH$%+############X  ,--=;-    
              -/H#####################H+=.     
                 .+#################X.         
               =%M####################H;.      
                  /@###############+;;/%%;,    
               -%###################$.         
             ;H######################M=        
          ,%#####MH$%;+#####M###-/@####%       
        :$H%+;=-      -####X.,H#   -+M##@-     
       .              ,###;    ;      =$##+    
                      .#H,               :XH,  
                       +                   .;- 

'''

ph6 = '''
                           -$-                 
                          .H##H,               
                         +######+              
                      .+#########H.            
                    -$############@.           
                  =H###############@  -X:      
                .$##################:  @#@-    
           ,;  .M###################;  H###;   
         ;@#:  @###################@  ,#####:  
       -M###.  M#################@.  ;######H  
       M####-  +###############$   =@#######X  
       H####$   -M###########+   :#########M,  
        /####X-   =########%   :M########@/.   
          ,;%H@X;   .$###X   :##MM@%+;:-       
                       ..                      
        -/;:-,.              ,,-==+M########H  
       -##################@HX%%+%%$%%%+:,,     
         .-/H%%%+%%$H@###############M@+=:/+:  
      /XHX%:#####MH%=    ,---:;;;;/%%XHM,:###$ 
      $@#MX %+;-                           .   

'''

ph7 = '''
                                           :X- 
                                        :X###  
                                      ;@####@  
                                    ;M######X  
                                  -@########$  
                                .$##########@  
                               =M############- 
                              +##############$ 
                            .H############$=.  
               ,/:         ,M##########M;.     
            -+@###;       =##########M;        
         =%M#######;     :#########M/          
      -$M###########;   :#########/            
       ,;X###########; =########$.             
           ;H#########+#######M=               
             ,+##############+                 
                /M#########@-                  
                  ;M######%                    
                    +####:                     
                     ,$M-                      

'''

ph8 = '''
                 .-;+$XHHHHHHX$+;-.            
              ,;X@@X%/;=----=:/%X@@X/,         
            =$@@%=.              .=+H@X:       
          -XMX:                      =XMX=     
         /@@:                          =H@+    
        %@X,                            .$@$   
       +@X.                               $@%  
      -@@,                                .@@= 
      %@%                                  +@$ 
      H@:                                  :@H 
      H@:         :HHHHHHHHHHHHHHHHHHX,    =@H 
      %@%         ;@M@@@@@@@@@@@@@@@@@H-   +@$ 
      =@@,        :@@@@@@@@@@@@@@@@@@@@@= .@@: 
       +@X        :@@@@@@@@@@@@@@@M@@@@@@:%@%  
        $@$,      ;@@@@@@@@@@@@@@@@@M@@@@@@$.  
         +@@HHHHHHH@@@@@@@@@@@@@@@@@@@@@@@+    
          =X@@@@@@@@@@@@@@@@@@@@@@@@@@@@X=     
            :$@@@@@@@@@@@@@@@@@@@M@@@@$:       
              ,;$@@@@@@@@@@@@@@@@@@X/-         
                 .-;+$XXHHHHHX$+;-.            

'''

ph9 = '''
                  ,:/+/-                       
                  /M/              .,-=;//;-   
             .:/= ;MH/,    ,=/+%$XH@MM#@:      
            -$##@+$###@H@MMM#######H:.    -/H# 
       .,H@H@ X######@ -H#####@+-     -+H###@  
        .,@##H;      +XM##M/,     =%@###@X;-   
      X%-  :M##########$.    .:%M###@%:        
      M##H,   +H@@@$/-.  ,;$M###@%,          - 
      M####M=,,---,.-%%H####M$:          ,+@## 
      @##################@/.         :%H##@$-  
      M###############H,         ;HM##M$=      
      #################.    .=$M##M$=          
      ################H..;XM##M$=          .:+ 
      M###################@%=           =+@MH% 
      @################M/.          =+H#X%=    
      =+M##############M,       -/X#X+;.       
        .;XM##########H=    ,/X#H+:,           
           .=+HM######M+/+HM@+=.               
               ,:/%XM####H/.                   
                    ,.:=-.                     

'''

ph10 = '''
              #+ @      # #              M#@   
        .    .X  X.%##@;# #   +@#######X. @#%  
          ,==.   ,######M+  -#####%M####M-    #
         :H##M%:=##+ .M##M,;#####/+#######% ,M#
        .M########=  =@#@.=#####M=M#######=  X#
        :@@MMM##M.  -##M.,#######M#######. =  M
                    @##..###:.    .H####. @@ X,
          ############: ###,/####;  /##= @#. M 
                  ,M## ;##,@#M;/M#M  @# X#% X# 
       .%=   ######M## ##.M#:   ./#M ,M #M ,#$ 
       ##/         $## #+;#: #### ;#/ M M- @# :
       #+ #M@MM###M-;M #:$#-##$H# .#X @ + $#. #
             ######/.: #%=# M#:MM./#.-#  @#: H#
       +,.=   @###: /@ %#,@  ##@X #,-#@.##% .@#
       #####+;/##/ @##  @#,+       /#M    . X, 
          ;###M#@ M###H .#M-     ,##M  ;@@; ###
          .M#M##H ;####X ,@#######M/ -M###$  -H
           .M###%  X####H  .@@MM@;  ;@#M@      
             H#M    /@####/      ,++.  / ==-,  
                      ,=/:, .+X@MMH@#H  #####$=

'''
# 定义要执行的函数
def execute_both_operations(mp3_path):
    # 创建两个线程，一个用于播放MP3，一个用于打印歌词
    mp3_thread = threading.Thread(target=play_mp3, args=(mp3_path,))
    lyrics_thread = threading.Thread(target=print_lyric, args=())
    credits_thread = threading.Thread(target=print_credits, args=(credits,))
    
    # 启动两个线程
    mp3_thread.start()
    lyrics_thread.start()
    credits_thread.start()

    # 等待两个线程都执行完毕
    mp3_thread.join()
    lyrics_thread.join()
    credits_thread.join()

################## Main ###################
print("\033[2J",end='')

#设置文本为绿色
print("\033[1;32m", end='')

build_frame1()

print_lyrics("Forms FORM-29827281-12:",2,2,0.1,0.1),
print_lyrics("Test Assessment Report",3,2,0.1,0.1),
print_lyrics("",4,2,0.1,2),  # Music start

# 调用函数
execute_both_operations(mp3_path)

#重置文本属性
print("\033[0m", end='')
print("\033[2J",end='')