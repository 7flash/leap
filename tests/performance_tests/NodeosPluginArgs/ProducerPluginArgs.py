#!/usr/bin/env python3

from dataclasses import dataclass
from BasePluginArgs import BasePluginArgs

@dataclass
class ProducerPluginArgs(BasePluginArgs):
    _pluginNamespace: str="eosio"
    _pluginName: str="producer_plugin"
    enableStaleProduction: bool=None
    _enableStaleProductionNodeosDefault: bool=False
    _enableStaleProductionNodeosArg: str="--enable-stale-production"
    pauseOnStartup: bool=None
    _pauseOnStartupNodeosDefault: bool=False
    _pauseOnStartupNodeosArg: str="--pause-on-startup"
    maxTransactionTime: int=None
    _maxTransactionTimeNodeosDefault: int=30
    _maxTransactionTimeNodeosArg: str="--max-transaction-time"
    maxIrreversibleBlockAge: int=None
    _maxIrreversibleBlockAgeNodeosDefault: int=-1
    _maxIrreversibleBlockAgeNodeosArg: str="--max-irreversible-block-age"
    producerName: str=None
    _producerNameNodeosDefault: str=None
    _producerNameNodeosArg: str="--producer-name"
    privateKey: str=None
    _privateKeyNodeosDefault: str=None
    _privateKeyNodeosArg: str="--private-key"
    signatureProvider: str=None
    _signatureProviderNodeosDefault: str="EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV=KEY:5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3"
    _signatureProviderNodeosArg: str="--signature-provider"
    greylistAccount: str=None
    _greylistAccountNodeosDefault: str=None
    _greylistAccountNodeosArg: str="--greylist-account"
    greylistLimit: int=None
    _greylistLimitNodeosDefault: int=1000
    _greylistLimitNodeosArg: str="--greylist-limit"
    produceTimeOffsetUs: int=None
    _produceTimeOffsetUsNodeosDefault: int=0
    _produceTimeOffsetUsNodeosArg: str="--produce-time-offset-us"
    lastBlockTimeOffsetUs: int=None
    _lastBlockTimeOffsetUsNodeosDefault: int=-200000
    _lastBlockTimeOffsetUsNodeosArg: str="--last-block-time-offset-us"
    cpuEffortPercent: int=None
    _cpuEffortPercentNodeosDefault: int=80
    _cpuEffortPercentNodeosArg: str="--cpu-effort-percent"
    lastBlockCpuEffortPercent: int=None
    _lastBlockCpuEffortPercentNodeosDefault: int=80
    _lastBlockCpuEffortPercentNodeosArg: str="--last-block-cpu-effort-percent"
    maxBlockCpuUsageThresholdUs: int=None
    _maxBlockCpuUsageThresholdUsNodeosDefault: int=5000
    _maxBlockCpuUsageThresholdUsNodeosArg: str="--max-block-cpu-usage-threshold-us"
    maxBlockNetUsageThresholdBytes: int=None
    _maxBlockNetUsageThresholdBytesNodeosDefault: int=1024
    _maxBlockNetUsageThresholdBytesNodeosArg: str="--max-block-net-usage-threshold-bytes"
    maxScheduledTransactionTimePerBlockMs: int=None
    _maxScheduledTransactionTimePerBlockMsNodeosDefault: int=100
    _maxScheduledTransactionTimePerBlockMsNodeosArg: str="--max-scheduled-transaction-time-per-block-ms"
    subjectiveCpuLeewayUs: int=None
    _subjectiveCpuLeewayUsNodeosDefault: int=31000
    _subjectiveCpuLeewayUsNodeosArg: str="--subjective-cpu-leeway-us"
    subjectiveAccountMaxFailures: int=None
    _subjectiveAccountMaxFailuresNodeosDefault: int=3
    _subjectiveAccountMaxFailuresNodeosArg: str="--subjective-account-max-failures"
    subjectiveAccountDecayTimeMinutes: int=None
    _subjectiveAccountDecayTimeMinutesNodeosDefault: int=1440
    _subjectiveAccountDecayTimeMinutesNodeosArg: str="--subjective-account-decay-time-minutes"
    incomingDeferRatio: int=None
    _incomingDeferRatioNodeosDefault: int=1
    _incomingDeferRatioNodeosArg: str="--incoming-defer-ratio"
    incomingTransactionQueueSizeMb: int=None
    _incomingTransactionQueueSizeMbNodeosDefault: int=1024
    _incomingTransactionQueueSizeMbNodeosArg: str="--incoming-transaction-queue-size-mb"
    disableSubjectiveBilling: int=None
    _disableSubjectiveBillingNodeosDefault: int=1
    _disableSubjectiveBillingNodeosArg: str="--disable-subjective-billing"
    disableSubjectiveAccountBilling: bool=None
    _disableSubjectiveAccountBillingNodeosDefault: bool=False
    _disableSubjectiveAccountBillingNodeosArg: str="--disable-subjective-account-billing"
    disableSubjectiveP2pBilling: int=None
    _disableSubjectiveP2pBillingNodeosDefault: int=1
    _disableSubjectiveP2pBillingNodeosArg: str="--disable-subjective-p2p-billing"
    disableSubjectiveApiBilling: int=None
    _disableSubjectiveApiBillingNodeosDefault: int=1
    _disableSubjectiveApiBillingNodeosArg: str="--disable-subjective-api-billing"
    producerThreads: int=None
    _producerThreadsNodeosDefault: int=2
    _producerThreadsNodeosArg: str="--producer-threads"
    snapshotsDir: str=None
    _snapshotsDirNodeosDefault: str='"snapshots"'
    _snapshotsDirNodeosArg: str="--snapshots-dir"

def main():
    pluginArgs = ProducerPluginArgs()
    print(pluginArgs.supportedNodeosArgs())
    exit(0)

if __name__ == '__main__':
    main()
