import video_game_edit

def test_choose_character():
    """ some happy path cases to test
    faculty_parking() """
    
    assert video_game_edit.choose_character("computer") == 1 or 2 or 3 or 4
    
test_choose_character()