#!/usr/bin/env python3

from dataclasses import dataclass
from .BasePluginArgs import BasePluginArgs

@dataclass
class HttpPluginArgs(BasePluginArgs):
    _pluginNamespace: str="eosio"
    _pluginName: str="http_plugin"
    unixSocketPath: str=None
    _unixSocketPathNodeosDefault: str=None
    _unixSocketPathNodeosArg: str="--unix-socket-path"
    httpServerAddress: str=None
    _httpServerAddressNodeosDefault: str="127.0.0.1:8888"
    _httpServerAddressNodeosArg: str="--http-server-address"
    httpsServerAddress: str=None
    _httpsServerAddressNodeosDefault: str=None
    _httpsServerAddressNodeosArg: str="--https-server-address"
    httpsCertificateChainFile: str=None
    _httpsCertificateChainFileNodeosDefault: str=None
    _httpsCertificateChainFileNodeosArg: str="--https-certificate-chain-file"
    httpsPrivateKeyFile: str=None
    _httpsPrivateKeyFileNodeosDefault: str=None
    _httpsPrivateKeyFileNodeosArg: str="--https-private-key-file"
    httpsEcdhCurve: str=None
    _httpsEcdhCurveNodeosDefault: str="secp384r1"
    _httpsEcdhCurveNodeosArg: str="--https-ecdh-curve"
    accessControlAllowOrigin: str=None
    _accessControlAllowOriginNodeosDefault: str=None
    _accessControlAllowOriginNodeosArg: str="--access-control-allow-origin"
    accessControlAllowHeaders: str=None
    _accessControlAllowHeadersNodeosDefault: str=None
    _accessControlAllowHeadersNodeosArg: str="--access-control-allow-headers"
    accessControlMaxAge: int=None
    _accessControlMaxAgeNodeosDefault: int=None
    _accessControlMaxAgeNodeosArg: str="--access-control-max-age"
    accessControlAllowCredentials: bool=None
    _accessControlAllowCredentialsNodeosDefault: bool=False
    _accessControlAllowCredentialsNodeosArg: str="--access-control-allow-credentials"
    maxBodySize: int=None
    _maxBodySizeNodeosDefault: int=2097152
    _maxBodySizeNodeosArg: str="--max-body-size"
    httpMaxBytesInFlightMb: int=None
    _httpMaxBytesInFlightMbNodeosDefault: int=500
    _httpMaxBytesInFlightMbNodeosArg: str="--http-max-bytes-in-flight-mb"
    httpMaxInFlightRequests: int=None
    _httpMaxInFlightRequestsNodeosDefault: int=-1
    _httpMaxInFlightRequestsNodeosArg: str="--http-max-in-flight-requests"
    httpMaxResponseTimeMs: int=None
    _httpMaxResponseTimeMsNodeosDefault: int=30
    _httpMaxResponseTimeMsNodeosArg: str="--http-max-response-time-ms"
    verboseHttpErrors: bool=None
    _verboseHttpErrorsNodeosDefault: bool=False
    _verboseHttpErrorsNodeosArg: str="--verbose-http-errors"
    httpValidateHost: int=None
    _httpValidateHostNodeosDefault: int=1
    _httpValidateHostNodeosArg: str="--http-validate-host"
    httpAlias: str=None
    _httpAliasNodeosDefault: str=None
    _httpAliasNodeosArg: str="--http-alias"
    httpThreads: int=None
    _httpThreadsNodeosDefault: int=2
    _httpThreadsNodeosArg: str="--http-threads"
    httpKeepAlive: int=None
    _httpKeepAliveNodeosDefault: int=1
    _httpKeepAliveNodeosArg: str="--http-keep-alive"

def main():
    pluginArgs = HttpPluginArgs()
    print(pluginArgs.supportedNodeosArgs())
    exit(0)

if __name__ == '__main__':
    main()
