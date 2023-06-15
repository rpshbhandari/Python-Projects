import airplane, Hour

class Flight_Log(airplane, Hour):
    def __init__(**kwargs):
        pass
    
    def create(self, **kwargs):
        pass







log_input = Flight_Log()

log_input.create(
    Flight_No = 101, 
    Flight_Date = '15/06/2023',
    Choke_Off = '12:40',
    Take_off = '12:45',
    Touch_down = '1:30',
    Choke_On = '1:45',
    PFI_Done = 'yes'
    )
