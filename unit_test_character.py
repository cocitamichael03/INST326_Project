#Big functions
import video_game_edit

def test_character():
    """ some happy path cases to test
    faculty_parking() """

    assert video_game_edit.character(1) == "Please choose attack: \n(1) Ash storm      (2) Rock smash\n(3) Volcanic blaze (4) +15 special.\nChoose (6) to exit.\n-----> "
    
test_character()