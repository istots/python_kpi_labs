print("Лабораторна робота 4. 9 варіант. Корсун Єлизавета, КМ-23")
print("Рядки. Завдання 1. Замінити всі символи a на d у словах, довжина яких менше 5 букв")
text = """ I ponder of something great
My lungs will fill and then deflate
They fill with fire, exhale desire
I know it's dire my time today
I have these thoughts, so often I ought
To replace that slot with what I once bought
'Cause somebody stole my car radio
and now I just sit in silence
Sometimes quiet is violent
I find it hard to hide it
My pride is no longer inside
It's on my sleeve
My skin will scream reminding me of
Who I killed inside my dream
I hate this car that I'm driving
There's no hiding for me
I'm forced to deal with what I feel
There is no distraction to mask what is real
I could pull the steering wheel
I have these thoughts, so often I ought
To replace that slot with what I once bought
'Cause somebody stole my car radio
and now I just sit in silence
I ponder of something terrifying
'Cause this time there's no sound to hide behind
I find over the course of our human existence
One thing consists of consistence
and it's that we're all battling fear
Oh dear, I don't know if we know why we're here
Oh my, too deep, please stop thinking
I liked it better when my car had sound
There are things we can do
But from the things that work there are only two
and from the two that we choose to do
Peace will win and fear will lose
It is faith and there's sleep
We need to pick one please because
Faith is to be awake
and to be awake is for us to think
and for us to think is to be alive
and I will try with every rhyme
To come across like I am dying
To let you know you need to try to think
I have these thoughts, so often I ought
To replace that slot with what I once bought
'Cause somebody stole my car radio
and now I just sit in silence  """

print('Текст до заміни: ', text)
print('')

text2 = text.split()

for ch in text2: 
    if len(ch) < 5:
        ch1 = ch.replace('a', 'd')
        text = text.replace(ch, ch1)

print('Текст після заміни: ', text)