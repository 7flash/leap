#!/usr/bin/env python3

import dataclasses
import re

from dataclasses import dataclass

@dataclass
class ChainPluginArgs:
    _pluginNamespace: str = "eosio"
    _pluginName: str = "chain_plugin"
    blocksDir: str=None
    _blocksDirNodeosDefault: str='"blocks"'
    _blocksDirNodeosArg: str="--blocks-dir"
    protocolFeaturesDir: str=None
    _protocolFeaturesDirNodeosDefault: str='"protocol_features"'
    _protocolFeaturesDirNodeosArg: str="--protocol-features-dir"
    checkpoint: str=None
    _checkpointNodeosDefault: str=None
    _checkpointNodeosArg: str="--checkpoint"
    wasmRuntime: str=None
    _wasmRuntimeNodeosDefault: str='eos-vm-jit'
    _wasmRuntimeNodeosArg: str="--wasm-runtime"
    profileAccount: str=None
    _profileAccountNodeosDefault: str=None
    _profileAccountNodeosArg: str="--profile-account"
    abiSerializerMaxTimeMs: int=None
    _abiSerializerMaxTimeMsNodeosDefault: int=15
    _abiSerializerMaxTimeMsNodeosArg: str="--abi-serializer-max-time-ms"
    chainStateDbSizeMb: int=None
    _chainStateDbSizeMbNodeosDefault: int=1024
    _chainStateDbSizeMbNodeosArg: str="--chain-state-db-size-mb"
    chainStateDbGuardSizeMb: int=None
    _chainStateDbGuardSizeMbNodeosDefault: int=128
    _chainStateDbGuardSizeMbNodeosArg: str="--chain-state-db-guard-size-mb"
    signatureCpuBillablePct: int=None
    _signatureCpuBillablePctNodeosDefault: int=50
    _signatureCpuBillablePctNodeosArg: str="--signature-cpu-billable-pct"
    chainThreads: int=None
    _chainThreadsNodeosDefault: int=2
    _chainThreadsNodeosArg: str="--chain-threads"
    contractsConsole: bool=None
    _contractsConsoleNodeosDefault: bool=False
    _contractsConsoleNodeosArg: str="--contracts-console"
    deepMind: bool=None
    _deepMindNodeosDefault: bool=False
    _deepMindNodeosArg: str="--deep-mind"
    actorWhitelist: str=None
    _actorWhitelistNodeosDefault: str=None
    _actorWhitelistNodeosArg: str="--actor-whitelist"
    actorBlacklist: str=None
    _actorBlacklistNodeosDefault: str=None
    _actorBlacklistNodeosArg: str="--actor-blacklist"
    contractWhitelist: str=None
    _contractWhitelistNodeosDefault: str=None
    _contractWhitelistNodeosArg: str="--contract-whitelist"
    contractBlacklist: str=None
    _contractBlacklistNodeosDefault: str=None
    _contractBlacklistNodeosArg: str="--contract-blacklist"
    actionBlacklist: str=None
    _actionBlacklistNodeosDefault: str=None
    _actionBlacklistNodeosArg: str="--action-blacklist"
    keyBlacklist: str=None
    _keyBlacklistNodeosDefault: str=None
    _keyBlacklistNodeosArg: str="--key-blacklist"
    senderBypassWhiteblacklist: str=None
    _senderBypassWhiteblacklistNodeosDefault: str=None
    _senderBypassWhiteblacklistNodeosArg: str="--sender-bypass-whiteblacklist"
    readMode: str=None
    _readModeNodeosDefault: str='head'
    _readModeNodeosArg: str="--read-mode"
    apiAcceptTransactions: int=None
    _apiAcceptTransactionsNodeosDefault: int=1
    _apiAcceptTransactionsNodeosArg: str="--api-accept-transactions"
    validationMode: str=None
    _validationModeNodeosDefault: str='full'
    _validationModeNodeosArg: str="--validation-mode"
    disableRamBillingNotifyChecks: bool=None
    _disableRamBillingNotifyChecksNodeosDefault: bool=False
    _disableRamBillingNotifyChecksNodeosArg: str="--disable-ram-billing-notify-checks"
    maximumVariableSignatureLength: int=None
    _maximumVariableSignatureLengthNodeosDefault: int=16384
    _maximumVariableSignatureLengthNodeosArg: str="--maximum-variable-signature-length"
    trustedProducer: str=None
    _trustedProducerNodeosDefault: str=None
    _trustedProducerNodeosArg: str="--trusted-producer"
    databaseMapMode: str=None
    _databaseMapModeNodeosDefault: str='mapped'
    _databaseMapModeNodeosArg: str="--database-map-mode"
    eosVmOcCacheSizeMb: int=None
    _eosVmOcCacheSizeMbNodeosDefault: int=1024
    _eosVmOcCacheSizeMbNodeosArg: str="--eos-vm-oc-cache-size-mb"
    eosVmOcCompileThreads: int=None
    _eosVmOcCompileThreadsNodeosDefault: int=1
    _eosVmOcCompileThreadsNodeosArg: str="--eos-vm-oc-compile-threads"
    eosVmOcEnable: bool=None
    _eosVmOcEnableNodeosDefault: bool=False
    _eosVmOcEnableNodeosArg: str="--eos-vm-oc-enable"
    enableAccountQueries: int=None
    _enableAccountQueriesNodeosDefault: int=0
    _enableAccountQueriesNodeosArg: str="--enable-account-queries"
    maxNonprivilegedInlineActionSize: int=None
    _maxNonprivilegedInlineActionSizeNodeosDefault: int=4096
    _maxNonprivilegedInlineActionSizeNodeosArg: str="--max-nonprivileged-inline-action-size"
    transactionRetryMaxStorageSizeGb: int=None
    _transactionRetryMaxStorageSizeGbNodeosDefault: int=None
    _transactionRetryMaxStorageSizeGbNodeosArg: str="--transaction-retry-max-storage-size-gb"
    transactionRetryIntervalSec: int=None
    _transactionRetryIntervalSecNodeosDefault: int=20
    _transactionRetryIntervalSecNodeosArg: str="--transaction-retry-interval-sec"
    transactionRetryMaxExpirationSec: int=None
    _transactionRetryMaxExpirationSecNodeosDefault: int=120
    _transactionRetryMaxExpirationSecNodeosArg: str="--transaction-retry-max-expiration-sec"
    transactionFinalityStatusMaxStorageSizeGb: int=None
    _transactionFinalityStatusMaxStorageSizeGbNodeosDefault: int=None
    _transactionFinalityStatusMaxStorageSizeGbNodeosArg: str="--transaction-finality-status-max-storage-size-gb"
    transactionFinalityStatusSuccessDurationSec: int=None
    _transactionFinalityStatusSuccessDurationSecNodeosDefault: int=180
    _transactionFinalityStatusSuccessDurationSecNodeosArg: str="--transaction-finality-status-success-duration-sec"
    transactionFinalityStatusFailureDurationSec: int=None
    _transactionFinalityStatusFailureDurationSecNodeosDefault: int=180
    _transactionFinalityStatusFailureDurationSecNodeosArg: str="--transaction-finality-status-failure-duration-sec"
    integrityHashOnStart: bool=None
    _integrityHashOnStartNodeosDefault: bool=False
    _integrityHashOnStartNodeosArg: str="--integrity-hash-on-start"
    integrityHashOnStop: bool=None
    _integrityHashOnStopNodeosDefault: bool=False
    _integrityHashOnStopNodeosArg: str="--integrity-hash-on-stop"
    blockLogRetainBlocks: int=None
    _blockLogRetainBlocksNodeosDefault: int=False
    _blockLogRetainBlocksNodeosArg: str="--block-log-retain-blocks"
    genesisJson: str=None
    _genesisJsonNodeosDefault: str=None
    _genesisJsonNodeosArg: str="--genesis-json"
    genesisTimestamp: str=None
    _genesisTimestampNodeosDefault: str=None
    _genesisTimestampNodeosArg: str="--genesis-timestamp"
    printGenesisJson: bool=None
    _printGenesisJsonNodeosDefault: bool=False
    _printGenesisJsonNodeosArg: str="--print-genesis-json"
    extractGenesisJson: bool=None
    _extractGenesisJsonNodeosDefault: bool=False
    _extractGenesisJsonNodeosArg: str="--extract-genesis-json"
    printBuildInfo: bool=None
    _printBuildInfoNodeosDefault: bool=False
    _printBuildInfoNodeosArg: str="--print-build-info"
    extractBuildInfo=None
    _extractBuildInfoNodeosDefault=None
    _extractBuildInfoNodeosArg: str="--extract-build-info"
    forceAllChecks: bool=None
    _forceAllChecksNodeosDefault: bool=False
    _forceAllChecksNodeosArg: str="--force-all-checks"
    disableReplayOpts: bool=None
    _disableReplayOptsNodeosDefault: bool=False
    _disableReplayOptsNodeosArg: str="--disable-replay-opts"
    replayBlockchain: bool=None
    _replayBlockchainNodeosDefault: bool=False
    _replayBlockchainNodeosArg: str="--replay-blockchain"
    hardReplayBlockchain: bool=None
    _hardReplayBlockchainNodeosDefault: bool=False
    _hardReplayBlockchainNodeosArg: str="--hard-replay-blockchain"
    deleteAllBlocks: bool=None
    _deleteAllBlocksNodeosDefault: bool=False
    _deleteAllBlocksNodeosArg: str="--delete-all-blocks"
    truncateAtBlock: int=None
    _truncateAtBlockNodeosDefault: int=0
    _truncateAtBlockNodeosArg: str="--truncate-at-block"
    terminateAtBlock: int=None
    _terminateAtBlockNodeosDefault: int=0
    _terminateAtBlockNodeosArg: str="--terminate-at-block"
    snapshot: str=None
    _snapshotNodeosDefault: str=None
    _snapshotNodeosArg: str="--snapshot"

    def threads(self, threads: int):
        self.chainThreads=threads

    def supportedNodeosArgs(self) -> list:
        args = []
        for field in dataclasses.fields(self):
            match = re.search("\w*NodeosArg", field.name)
            if match is not None:
                args.append(getattr(self, field.name))
        return args

    def __str__(self) -> str:
        args = [] 
        for field in dataclasses.fields(self):
            match = re.search("[^_]", field.name[0])
            if match is not None:
                default = getattr(self, f"_{field.name}NodeosDefault")
                current = getattr(self, field.name)
                if current is not None and current != default:
                    if type(current) is bool:
                        args.append(f"{getattr(self, f'_{field.name}NodeosArg')}")
                    else:
                        args.append(f"{getattr(self, f'_{field.name}NodeosArg')} {getattr(self, field.name)}")

        return "--plugin " + self._pluginNamespace + "::" + self._pluginName + " " + " ".join(args) if len(args) > 0 else ""

def main():
    pluginArgs = ChainPluginArgs()
    print(pluginArgs.supportedNodeosArgs())
    exit(0)

if __name__ == '__main__':
    main()
