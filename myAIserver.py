import os
import openai

import anvil.server

anvil.server.connect("LYA3ZG7QSXBQM5E6Z673E36Y-GOL24TLVYNQIMUHQ")
openai.api_key = "sk-DJxYSICFKQrbDRQ7buJXvlDfzpjOEO8WqGWgTj1D"

import anvil.media

@anvil.server.callable
def say_hello(name):
  print(name)
  myPrompt = name + "\n"

  response = openai.Completion.create(
    engine="davinci",
    prompt="How much are we getting?\nham\nIs ur paper in e morn or aft tmr?\nham\nDear relieved of westonzoyland, all going to plan this end too!\nham\nHope you are having a great new semester. Do wish you the very best. You are made for greatness.\nham\nOh yes I can speak txt 2 u no! Hmm. Did u get  email?\nham\nI want to show you the world, princess :) how about europe?\nham\nNobody can decide where to eat and dad wants Chinese\nham\nNo shoot me. I'm in the docs waiting room. :/\nham\nNow? I'm going out 4 dinner soon..\nham\nHello which the site to download songs its urgent pls\nham\nI do know what u mean,  is the king of not havin credit! I'm goin2bed now. Night night sweet! Only1more sleep! \nham\nHorrible gal. Me in sch doing some stuff. How come u got mc?\nham\nHI HUN! IM NOT COMIN 2NITE-TELL EVERY1 IM SORRY 4 ME, HOPE U AVA GOODTIME!OLI RANG MELNITE IFINK IT MITE B SORTED,BUT IL EXPLAIN EVERYTHIN ON MON.L8RS.x\nham\nI call you later, don't have network. If urgnt, sms me.\nham\nUmmmmmaah Many many happy returns of d day my dear sweet heart.. HAPPY BIRTHDAY dear\nham\nPlease CALL 08712402779 immediately as there is an urgent message waiting for you\nspam\nYeah like if it goes like it did with my friends imma flip my shit in like half an hour\nham\nMum say we wan to go then go... Then she can shun bian watch da glass exhibition... \nham\nWhat your plan for pongal?\nham\nJust wait till end of march when el nino gets himself. Oh.\nham\nNot yet chikku..going to room nw, i'm in bus..\nham\nAm also doing in cbe only. But have to pay.\nham\nHoney boo I'm missing u.\nham\nWe have sent JD for Customer Service cum Accounts Executive to ur mail id, For details contact us\nham\nYo, I'm at my parents' gettin cash. Good news: we picked up a downstem\nham\nThank you so much. When we skyped wit kz and sura, we didnt get the pleasure of your company. Hope you are good. We've given you ultimatum oh! We are countin down to aburo. Enjoy!\nham\nHungry gay guys feeling hungry and up 4 it, now. Call 08718730555 just 10p/min. To stop texts call 08712460324 (10p/min)\nspam\nOk. No wahala. Just remember that a friend in need ...\nham\nI will see in half an hour\nham\nIm in inperialmusic listening2the weirdest track ever byåÓleafcutter johnåÓ-sounds like insects being molested&someone plumbing,remixed by evil men on acid!\nham\n\Hey sorry I didntgive ya a a bellearlier hunny\nham\nSERIOUSLY. TELL HER THOSE EXACT WORDS RIGHT NOW.\nham\nCan U get 2 phone NOW? I wanna chat 2 set up meet Call me NOW on 09096102316 U can cum here 2moro Luv JANE xx Callså£1/minmoremobsEMSPOBox45PO139WA\nspam\nTee hee. Off to lecture, cheery bye bye.\nham\nSorry chikku, my cell got some problem thts y i was nt able to reply u or msg u..\nham\nIf you still havent collected the dough pls let me know so i can go to the place i sent it to get the control number\nham\nOk...\nham\nnetwork operator. The service is free. For T & C's visit 80488.biz\nspam\nLet me know how to contact you. I've you settled in a room. Lets know you are ok.\nham\nWot u up 2 u weirdo?\nham\nCan do lor...\nham\nDont put your phone on silent mode ok\nham\nCan i meet Ì_ at 5.. As 4 where depends on where Ì_ wan 2 in lor..\nham\nWaiting 4 my tv show 2 start lor... U leh still busy doing ur report?\nham\nOh ho. Is this the first time u use these type of words\nham\nAm I the only one who doesn't stalk profiles?\nham\nEver green quote ever told by Jerry in cartoon \A Person Who Irritates u Always Is the one Who Loves u Vry Much But Fails to Express It...!..!! :-) :-) gud nyt\"\nham\nYes i thought so. Thanks.\nham\nBut if she.s drinkin i'm ok.\nham\nJust wondering, the others just took off\nham\nNight has ended for another day, morning has come in a special way. May you smile like the sunny rays and leaves your worries at the blue blue bay. Gud mrng\nham\nWhat do you do, my dog ? Must I always wait till the end of your day to have word from you ? Did you run out of time on your cell already?\nham\nHappy new year to u too!\nham\nHey...Great deal...Farm tour 9am to 5pm $95/pax, $50 deposit by 16 May\nham\n" + myPrompt,
    temperature=0.7,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n"]
  )
  myResponse = response["choices"]
  myText = myResponse[0]
  realText = myText["text"]
  print(realText)
  return realText

anvil.server.wait_forever()
