import random
import colorama
import os

colorama.init()

def generate_pickup_line():
  """Generates a pickup line."""
  pickup_lines = [
      f"Are you a parking ticket? Because you've got fine written all over you {colorama.Fore.YELLOW}.",
      f"Are you a dictionary? Because you're adding meaning to my life {colorama.Fore.CYAN}.",
      f"Are you a mirror? Because I can see myself in your eyes {colorama.Fore.MAGENTA}.",
      f"Are you a fireman? Because you're making me hot {colorama.Fore.RED}.",
      f"Are you a banana? Because I find you a-peeling {colorama.Fore.BLUE}.",
      f"Are you a library book? Because I want to check you out {colorama.Fore.GREEN}.",
      f"Are you a parking meter? Because I'd like to feed you my coins {colorama.Fore.YELLOW}.",
      f"Are you a dictionary? Because you're giving me the definition of love {colorama.Fore.CYAN}.",
      f"Are you a camera? Because I'd like to take a picture of you with my heart {colorama.Fore.MAGENTA}.",
      f"Are you a broom? Because you sweep me off my feet {colorama.Fore.RED}.",
      f"Are you a time traveler? Because I see you in my future. {colorama.Fore.RED}.",
      f"Are you a dream? Because you're so beautiful, I don't want to wake up. {colorama.Fore.CYAN}.",
      f"Are you a history book? Because I'd like to learn more about you. {colorama.Fore.BLUE}.",
      f"Are you a ghost? Because you're haunting my dreams {colorama.Fore.GREEN}.",
      f"Are you a hurricane? Because you're blowing me away. {colorama.Fore.GREEN}.",
      f"Are you a mirror? Because I can see myself in your eyes. {colorama.Fore.GREEN}.",
      f"Are you a fire alarm? Because you're really quite a sizzling sensation. {colorama.Fore.GREEN}.",
      f"Are you a volcano? Because you're hot and you make me wanna erupt. {colorama.Fore.GREEN}.",
      f"Are you a wizard? Because you've cast a spell on me. {colorama.Fore.GREEN}.",
      f"Are you a work of art? Because you're a masterpiece. {colorama.Fore.GREEN}.",
      f"Are you a celebrity? Because you're definitely a star. {colorama.Fore.BLUE}.",
      f"Are you a fireman? Because you're making me hot. {colorama.Fore.GREEN}.",
      f"Are you a helicopter? Because I'm feeling a little turned on. {colorama.Fore.GREEN}.",
      f"Are you a knight in shining armor? Because I need you to save me from this boring conversation. {colorama.Fore.GREEN}.",
      f"Are you a chameleon?  you change colors every time I look at you. {colorama.Fore.YELLOW}.",
      f"Are you a genie? Because I'd like to make a wish. {colorama.Fore.GREEN}.",
      f"Are you a yo-yo? Because I can't keep my eyes off of you. {colorama.Fore.GREEN}.",
      f"Are you a zombie? Because you're looking pretty dead to me. {colorama.Fore.GREEN}.",
      f"Are you a time machine? Because I'd like to go back in time and meet you sooner. {colorama.Fore.GREEN}.",
      f"Are you a star? Because you're shining so bright. {colorama.Fore.GREEN}.",
      f"Are you a parking meter? Because I'd like to feed you my coins. {colorama.Fore.GREEN}.",
      f"Are you a rainbow? Because you're definitely something to look at. {colorama.Fore.GREEN}.",
      f"Are you a cloud? Because I'm feeling a connection with you {colorama.Fore.GREEN}.",


  ]
  return random.choice(pickup_lines)
os.system('xdg-open https://t.me/termux_command_store')
def main():
  while True:
    pickup_line = generate_pickup_line()
    os.system('clear')
    print(pickup_line)
    input("Press Enter to generate another pickup line.TAKE LOVE FROM TCS (TERMUX_COMMAND_STORE)")
    os.system('clear')
if __name__ == "__main__":
  main()
  