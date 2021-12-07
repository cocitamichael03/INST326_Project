def char(chr_numb):
    """
        Allows user to choose the kind of
    attack fortheir selected character. 
    
    Args: 
         chr_numb: Accepts int one through six. 

    Returns:
         chr_numb == 1 : The attack options for Volcamore and an exit option.
         chr_numb == 2 : The attack options for Falconstein and an exit option. 
         chr_numb == 3 : The attack options for Gasmosphere and an exit option. 
         chr_numb == 4 : The attack options for Atomic Tin and an exit option. 
    """
    
    if chr_numb == 1: #Volcamore
        return f"Please choose attack: \n(1) Ash storm      (2) Rock smash\n(3) Volcanic blaze (4) +15 special.\nChoose (6) to exit.\n-----> "
    
    if chr_numb == 2: #Falconstein 
        return f"Please choose attack: \n(1) Birdseye       (2) Big punch \n(3) Volcanic blaze (4) +15 special.\nChoose (6) to exit.\n-----> "
    if chr_numb == 3: #Gasmosphere
        return f"Please choose attack: \n(1) Gas mist       (2) Fiery breeze\n(3) Forest fire  (4) +15 special.\nChoose (6) to exit.\n-----> "
    if chr_numb == 4: #Atomic Tic
        return f"Please choose attack: \n(1) Explode        (2) Radiactice wave\n(3) Atomic bomb (4) +15 special.\nChoose (6) to exit.\n-----> "

