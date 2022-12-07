#!/usr/bin/env python3

from dataclasses import dataclass
from BasePluginArgs import BasePluginArgs

@dataclass
class NetPluginArgs(BasePluginArgs):
    _pluginNamespace: str="eosio"
    _pluginName: str="net_plugin"
    p2pListenEndpoint: str=None
    _p2pListenEndpointNodeosDefault: str="0.0.0.0:9876"
    _p2pListenEndpointNodeosArg: str="--p2p-listen-endpoint"
    p2pServerAddress: str=None
    _p2pServerAddressNodeosDefault: str=None
    _p2pServerAddressNodeosArg: str="--p2p-server-address"
    p2pPeerAddress: str=None
    _p2pPeerAddressNodeosDefault: str=None
    _p2pPeerAddressNodeosArg: str="--p2p-peer-address"
    p2pMaxNodesPerHost: int=None
    _p2pMaxNodesPerHostNodeosDefault: int=1
    _p2pMaxNodesPerHostNodeosArg: str="--p2p-max-nodes-per-host"
    p2pAcceptTransactions: int=None
    _p2pAcceptTransactionsNodeosDefault: int=1
    _p2pAcceptTransactionsNodeosArg: str="--p2p-accept-transactions"
    agentName: str=None
    _agentNameNodeosDefault: str="EOS Test Agent"
    _agentNameNodeosArg: str="--agent-name"
    allowedConnection: str=None
    _allowedConnectionNodeosDefault: str="any"
    _allowedConnectionNodeosArg: str="--allowed-connection"
    peerKey: str=None
    _peerKeyNodeosDefault: str=None
    _peerKeyNodeosArg: str="--peer-key"
    peerPrivateKey: str=None
    _peerPrivateKeyNodeosDefault: str=None
    _peerPrivateKeyNodeosArg: str="--peer-private-key"
    maxClients: int=None
    _maxClientsNodeosDefault: int=25
    _maxClientsNodeosArg: str="--max-clients"
    connectionCleanupPeriod: int=None
    _connectionCleanupPeriodNodeosDefault: int=30
    _connectionCleanupPeriodNodeosArg: str="--connection-cleanup-period"
    maxCleanupTimeMsec: int=None
    _maxCleanupTimeMsecNodeosDefault: int=10
    _maxCleanupTimeMsecNodeosArg: str="--max-cleanup-time-msec"
    p2pDedupCacheExpireTimeSec: int=None
    _p2pDedupCacheExpireTimeSecNodeosDefault: int=10
    _p2pDedupCacheExpireTimeSecNodeosArg: str="--p2p-dedup-cache-expire-time-sec"
    netThreads: int=None
    _netThreadsNodeosDefault: int=2
    _netThreadsNodeosArg: str="--net-threads"
    syncFetchSpan: int=None
    _syncFetchSpanNodeosDefault: int=100
    _syncFetchSpanNodeosArg: str="--sync-fetch-span"
    useSocketReadWatermark: int=None
    _useSocketReadWatermarkNodeosDefault: int=0
    _useSocketReadWatermarkNodeosArg: str="--use-socket-read-watermark"
    peerLogFormat: str=None
    _peerLogFormatNodeosDefault: str='["${_name}" - ${_cid} ${_ip}:${_port}] '
    _peerLogFormatNodeosArg: str="--peer-log-format"
    p2pKeepaliveIntervalMs: int=None
    _p2pKeepaliveIntervalMsNodeosDefault: int=10000
    _p2pKeepaliveIntervalMsNodeosArg: str="--p2p-keepalive-interval-ms"

    def threads(self, threads: int):
        self.netThreads=threads

def main():
    pluginArgs = NetPluginArgs()
    print(pluginArgs.supportedNodeosArgs())
    exit(0)

if __name__ == '__main__':
    main()
