( Please view with a mono-spaced font )

# --------------------------------------------------------- #
#                      <<  Ethereal  >>                     #
#                  A Discord Token Grabber                  #
#                                                           #
#                  Coded with <3 by 80xh34d                 #
#                 https://github.com/80xh34d                #
#                  Last updated 21.06.2022                  #
#                                                           #
#                        :: About ::                        #
# The goal of this project is to understand how attackers   #
# can gain access to someone's Discord account via their    #
# authentication token, as well as preventative measures.   #
#                                                           #
#                      :: Disclaimer ::                     #
# This project was made solely for educational purposes.    #
# I am not responsible for anything that happens to you or  #
# your Discord account as a result of this program.         #
# Do not use this script on real people to try to grab      #
# people's auth tokens or other information. If you do so,  #
# Discord will rightfully ban your account.                 #
#                                                           #
# Token grabbing is AGAINST Discord's Community Guidelines  #
# and Terms of Service.                                     #
# Please review Discord's guidelines here:                  #
#   • https://dis.gd/terms                                  #
#   • https://dis.gd/guidelines                             #
#                                                           #
# If you believe that you are victim to a token grabber,    #
# change your password immediately to reset your token.     #
#                                                           #
#                       :: Program ::                       #
# When ran, the program will begin scanning the victim's    #
# leveldb directories, which contain log files that store   #
# the victim's Discord authorisation token. Once the files  #
# are located, they are searched with a regex pattern to    #
# yield any valid auth tokens. These auth tokens are then   #
# sent to the attacker via a Discord webhook API URL that   #
# is connected to one of the attacker's Discord servers.    #
#                                                           #
#                       :: Warning ::                       #
# This attack is especially precarious because Discord's    #
# auth tokens allow the attacker to directly log into the   #
# victim's Discord account while also bypassing all account #
# verification such as password, email, IP verify, or MFA.  #
# Along with the victim's auth tokens, the grabber has the  #
# capability of sending other sensitive information about   #
# the victim to the attacker such as their saved browser    #
# passwords and cookies, their system information, their IP #
# address and location information, et cetera.              #
#                                                           #
#                      :: Prevention ::                     #
# The key method of preventing attacks like token grabbers  #
# is to--obviously--not run untrusted files on your PC.     #
# Attackers can't get you if you don't give them a chance.  #
# Apart from that, you could employ methods to protect your #
# Local Storage (leveldb) so that attackers can't read it.  #
# Note that Discord reads Local Storage and leveldb to sign #
# into your account on launch.                              #
#                                                           #
# I strongly reccomend andro2157's Discord Token Protector: #
#   • https://github.com/andro2157/DiscordTokenProtector    #
#                                                           #
# Thank you for taking the time to read this. Suggestions   #
# on how to improve this message can be sent on GitHub.     #
#                                                           #
# -- A message from 80xh34d (need to move to a readme file) #
# --------------------------------------------------------- #
