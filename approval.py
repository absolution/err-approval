# errbot issue - Support peer approval of bot commands #948

import threading
import uuid

from errbot import BotPlugin, botcmd, cmdfilter

def ident(msg):
    """ Retreive the relevant identity for Approval from the given message."""
    # if the identity requires a special field to be used for acl
    return msg.frm.aclattr if hasattr(msg.frm, 'aclattr') else msg.frm.person

def make_approval_code():
    """ Make a unique approval code """
    return str(uuid.uuid1()).replace("-", "")
    # return '\n'.join(line.lstrip() for line in sio.getvalue().split('\n'))

class Approval(BotPlugin):
    """ Implements command approvals for Errbot. """
    def __init__(self, bot):
        super().__init__(bot)
        self.pending = []  # pending commands awaiting approval
        self.lock = threading.Lock()
        self.pending_lock = threading.Lock()
