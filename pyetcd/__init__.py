# -*- coding: utf-8 -*-

__author__ = 'TwinDB Development Team'
__email__ = 'dev@twindb.com'
__version__ = '0.1.0'


class EtcdResult(object):
    """
    Response from Etcd API
    """
    def __init__(self, payload):
        """
        Initialise EtcdResult instance

        :param payload: JSON string with response from Etcd
        ::
            {
                "action": "set",
                "node": {
                    "createdIndex": 2,
                    "key": "/message",
                    "modifiedIndex": 2,
                    "value": "Hello world"
                }
            }
        """

    @property
    def node(self):
        return self.node

    @property
    def prev_node(self):
        return self.prev_node


class ResponseNode(object):
    """
    Etcd response includes information about nodes.
    """

    def __init__(self, key, value=None,
                 created_index=None,
                 modified_index=None):
        """
        Initialise ResponseNode instance

        :param key: the HTTP path to which the request was made.
        We set /message to Hello world, so the key field is /message.
        etcd uses a file-system-like structure to represent
        the key-value pairs, therefore all keys start with /.
        :param value: the value of the key after resolving the request.
        :param created_index: an index is a unique, monotonically-incrementing
        integer created for each change to etcd. This specific index reflects
        the point in the etcd state member at which a given key was created
        :param modified_index: like node.createdIndex, this attribute is also
        an etcd index. Actions that cause the value to change include set,
        delete, update, create, compareAndSwap and compareAndDelete.
        Since the get and watch commands do not change state in the store,
        they do not change the value of node.modifiedIndex.
        """
        self.modifiedIndex = modified_index
        self.createdIndex = created_index
        self.value = value
        self.key = key


# Exceptions

class EtcdException(Exception):
    """
    Generic Etcd error.
    """


class EtcdTestFailed(EtcdException):
    """
    Error EcodeTestFailed (http code 101)
    """


class EtcdNotFile(EtcdException):
    """
    Error EcodeNotFile (http code 102)
    """


class EtcdNoMorePeer(EtcdException):
    """
    Error ecodeNoMorePeer (http code 103)
    """


class EtcdNotDir(EtcdException):
    """
    Error EcodeNotDir (http code 104)
    """


class EtcdNodeExist(EtcdException):
    """
    Error EcodeNodeExist (http code 105)
    """


class EtcdKeyIsPreserved(EtcdException):
    """
    Error ecodeKeyIsPreserved (http code 106)
    """


class EtcdRootROnly(EtcdException):
    """
    Error EcodeRootROnly (http code 107)
    """


class EtcdDirNotEmpty(EtcdException):
    """
    Error EcodeDirNotEmpty (http code 108)
    """


class EtcdExistingPeerAddr(EtcdException):
    """
    Error ecodeExistingPeerAddr (http code 109)
    """


class EtcdUnauthorized(EtcdException):
    """
    Error EcodeUnauthorized (http code 110)
    """


class EtcdValueRequired(EtcdException):
    """
    Error ecodeValueRequired (http code 200)
    """


class EtcdPrevValueRequired(EtcdException):
    """
    Error EcodePrevValueRequired (http code 201)
    """


class EtcdTTLNaN(EtcdException):
    """
    Error EcodeTTLNaN (http code 202)
    """


class EtcdIndexNaN(EtcdException):
    """
    Error EcodeIndexNaN (http code 203)
    """


class EtcdValueOrTTLRequired(EtcdException):
    """
    Error ecodeValueOrTTLRequired (http code 204)
    """


class EtcdTimeoutNaN(EtcdException):
    """
    Error ecodeTimeoutNaN (http code 205)
    """


class EtcdNameRequired(EtcdException):
    """
    Error ecodeNameRequired (http code 206)
    """


class EtcdIndexOrValueRequired(EtcdException):
    """
    Error ecodeIndexOrValueRequired (http code 207)
    """


class EtcdIndexValueMutex(EtcdException):
    """
    Error ecodeIndexValueMutex (http code 208)
    """


class EtcdInvalidField(EtcdException):
    """
    Error EcodeInvalidField (http code 209)
    """


class EtcdInvalidForm(EtcdException):
    """
    Error EcodeInvalidForm (http code 210)
    """


class EtcdRefreshValue(EtcdException):
    """
    Error EcodeRefreshValue (http code 211)
    """


class EtcdRefreshTTLRequired(EtcdException):
    """
    Error EcodeRefreshTTLRequired (http code 212)
    """


class EtcdRaftInternal(EtcdException):
    """
    Error EcodeRaftInternal (http code 300)
    """


class EtcdLeaderElect(EtcdException):
    """
    Error EcodeLeaderElect (http code 301)
    """


class EtcdWatcherCleared(EtcdException):
    """
    Error EcodeWatcherCleared (http code 400)
    """


class EtcdEventIndexCleared(EtcdException):
    """
    Error EcodeEventIndexCleared (http code 401)
    """


class EtcdStandbyInternal(EtcdException):
    """
    Error ecodeStandbyInternal (http code 402)
    """


class EtcdInvalidActiveSize(EtcdException):
    """
    Error ecodeInvalidActiveSize (http code 403)
    """


class EtcdInvalidRemoveDelay(EtcdException):
    """
    Error ecodeInvalidRemoveDelay (http code 404)
    """


class EtcdClientInternal(EtcdException):
    """
    Error ecodeClientInternal (http code 500)
    """


