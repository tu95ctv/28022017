//================================================================//
// Project           : Ung cuu                          //
// Created By        :  OMCKV2 VNP2                             //
// Date/Time Created : {{site3g.now}}-->
// Site Name         : 3G_{{site3g.Site_Name_1}}                           //
// Site ID           : {{site3g.Site_ID_3G}}                               //
// RBS ID            : {{site3g.id_n}}                                  //
//================================================================//
// Running at Node       : RBS                                    //
//================================================================//
CREATE
(
    parent "ManagedElement=1,IpSystem=1"
    identity "1"
    moType IpAccessSctp
    exception none
    nrOfAttributes 2
        userLabel String "IpAccessSctp_1"
        ipAccessHostEtRef1 Ref "ManagedElement=1,IpSystem=1,IpAccessHostEt=1"
)
CREATE
(
    parent "ManagedElement=1,TransportNetwork=1"
    identity "1"
    moType Sctp
    exception none
    nrOfAttributes 13
        userLabel String "Sctp_1"
        numberOfAssociations Integer 2
        minimumRto Integer 10
        maximumRto Integer 40
        initialRto Integer 20
        associationMaxRtx Integer 12
        pathMaxRtx Integer 6
        maxUserDataSize Integer 556
        mBuffer Integer 16
        nThreshold Integer 12
        initialAdRecWin Integer 16384
        rpuId Ref "ManagedElement=1,SwManagement=1,ReliableProgramUniter=sctp_host"
        ipAccessSctpRef Ref "ManagedElement=1,IpSystem=1,IpAccessSctp=1"
)
CREATE
(
    parent "ManagedElement=1,NodeBFunction=1"
    identity "b{{site3g.id_n}}"
    moType Iub
    exception none
    nrOfAttributes 4
        controlPlaneTransportOption Struct
        nrOfElements 2
            atm Boolean false
            ipV4 Boolean true
        userPlaneTransportOption Struct
        nrOfElements 2
            atm Boolean false
            ipV4 Boolean true
        rbsId Integer {{site3g.id_n}}
        userPlaneIpResourceRef Ref "ManagedElement=1,IpSystem=1,IpAccessHostEt=1"
)
SET
  (
  mo "ManagedElement=1,Equipment=1,Subrack=1,Slot=2,PlugInUnit=1,ExchangeTerminalIp=1,EthernetSwitch=1,EthernetSwitchPort=6"
  exception none
  operatingMode Struct
     nrOfElements 2
     autoNegotiation Boolean true
     configuredSpeedDuplex Integer 4 
  )
SET
  (
  mo "ManagedElement=1,Equipment=1,Subrack=1,Slot=2,PlugInUnit=1,ExchangeTerminalIp=1,EthernetSwitch=1,EthernetSwitchPort=6"
  exception none
  ingressPeakBitrate Integer 1000
  )
CREATE
(
    parent "ManagedElement=1,NodeBFunction=1,Iub=b{{site3g.id_n}}"
    identity "1"
    moType NbapCommon
    exception none
    nrOfAttributes 4
        l2EstablishReqRetryT Integer 1
        auditRetransmissionT Integer 5
        l2EstablishSupervisionT Integer 30
        l3EstablishSupervisionT Integer 30
)
CREATE
(
    parent "ManagedElement=1,NodeBFunction=1,Iub=b{{site3g.id_n}}"
    identity "1"
    moType NbapDedicated
    exception none
    nrOfAttributes 2
        l2EstablishReqRetryT Integer 1
        l2EstablishSupervisionT Integer 30
)
SET
  (
  mo "ManagedElement=1,NodeBFunction=1,Iub=b{{site3g.id_n}},IubDataStreams=1"
  exception none
  maxHsRate Integer 100
  )
