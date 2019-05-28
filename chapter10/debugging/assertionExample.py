#! python3

# an assertion is a sanity check to make sure the code isn't doing something obviously wrong
#   assertions can be disabled on the cmd line by adding the -0 flag

def makeAssert():
    assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'

podBayDoorStatus = 'open'
makeAssert()

podBayDoorStatus = "I'm sorry, Dave. I'm afraid I can't do that."
makeAssert()
