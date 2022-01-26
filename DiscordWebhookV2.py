from dhooks import Webhook, Embed
import time
TheWebHook = Webhook("PUTYOURWEBHOOKHERE")
neco = "https://media.discordapp.net/attachments/759572977770692627/935722923191324682/copim.jpeg"
IMGorMSG = int(input("Message[1], Image[2] choose: "))
#credit to dhook team helped me a lot! 
#dhook github https://github.com/kyb3r/dhooks
#Version 2 (V3 WHEN?)
if IMGorMSG == 1 :
    embed = Embed(
    description = ("dont click random links"),
    color = 0xff0000,
    timestamp = 'now' 
    )
    embed.add_field(name = 'Message:', value = input("Say yo bullshit: ")) 
    TheWebHook.send(embed = embed)
elif IMGorMSG == 2: 
    UserInputIMG = input("COPY AND PASTE YOUR PHOTO AS A DISCORD HOSTED LINK: ")
    embed = Embed(
    description = 'Image: ',
    timestamp = 'now' 
    )
    embed.set_image(UserInputIMG)
    TheWebHook.send(embed=embed)
time.sleep(3)
