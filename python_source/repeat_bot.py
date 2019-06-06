#############################################################################
# repeat_bot.py
#----------------------------------------------------------------------------
# Posts the most recent image from a folder of images, deletes it and
# exits.
#############################################################################

import sys, time, logging, os

from TwitterConnection.twitter_connection import TwitterConnection

#----------------------------------------------------------------------------

IMAGES_PATH = os.path.join ( "images" )

#----------------------------------------------------------------------------

def post_image ( tc ):
    
    #tc.send_message_chain ( [ "Hello from python." ] )

    is_png = lambda x : isinstance ( x, str ) and \
                        len ( x ) > 4         and \
                        x [ -4 : ] == '.png'

    image_files = filer ( is_png, os.listdir ( IMAGES_PATH ) )

    logging.info ( str ( image_files ) )

#----------------------------------------------------------------------------

def handle_exceptions ( exc_type, exc_value, exc_traceback ):
    """
    Used to log uncaught exceptions."
    """

    if issubclass ( exc_type, KeyboardInterrupt ):

        sys.__excepthook__ ( exc_type, exc_value, exc_traceback )
        return

    logging.critical ( "Unhandled Exception", 
                      exc_info = ( exc_type, exc_value, exc_traceback ) )
#----------------------------------------------------------------------------

def main ():

    logging.basicConfig ( format='%(asctime)s - %(levelname)s - %(message)s', 
                          level=logging.INFO )

    sys.excepthook = handle_exceptions
    
    logging.info ( "Repeat Bot" )

    logging.info ( "Creating Twitter Connection" )

    with TwitterConnection () as tc:

        post_image ( tc )


if __name__ == "__main__":
    sys.exit ( main () )
