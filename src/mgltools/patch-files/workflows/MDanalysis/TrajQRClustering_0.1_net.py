#!/bin/ksh ~/.mgltools/pythonsh
########################################################################
#
#    Vision Network - Python source code - file generated by vision
#    Wednesday 23 February 2011 12:30:54 
#    
#       The Scripps Research Institute (TSRI)
#       Molecular Graphics Lab
#       La Jolla, CA 92037, USA
#
# Copyright: Daniel Stoffler, Michel Sanner and TSRI
#   
# revision: Guillaume Vareille
#  
#########################################################################
#
# $Header: /home/cvs/CVSROOT/nbcr/src/roll/autodock/src/mgltools/patch-files/workflows/MDanalysis/Attic/TrajQRClustering_0.1_net.py,v 1.1 2012/02/07 22:50:29 clem Exp $
#
# $Id: TrajQRClustering_0.1_net.py,v 1.1 2012/02/07 22:50:29 clem Exp $
#


if __name__=='__main__':
    from sys import argv
    if '--help' in argv or '-h' in argv or '-w' in argv: # run without Vision
        withoutVision = True
        from Vision.VPE import NoGuiExec
        ed = NoGuiExec()
        from NetworkEditor.net import Network
        import os
        masterNet = Network("process-"+str(os.getpid()))
        ed.addNetwork(masterNet)
    else: # run as a stand alone application while vision is hidden
        withoutVision = False
        from Vision import launchVisionToRunNetworkAsApplication, mainLoopVisionToRunNetworkAsApplication
	if '-noSplash' in argv:
	    splash = False
	else:
	    splash = True
        masterNet = launchVisionToRunNetworkAsApplication(splash=splash)
        import os
        masterNet.filename = os.path.abspath(__file__)
from traceback import print_exc
## loading libraries ##
from AutoDockTools.VisionInterface.Adt import Adt
from WebServices.VisionInterface.WSNodes import wslib
from Vision.StandardNodes import stdlib
try:
    masterNet
except (NameError, AttributeError): # we run the network outside Vision
    from NetworkEditor.net import Network
    masterNet = Network()

masterNet.getEditor().addLibraryInstance(Adt,"AutoDockTools.VisionInterface.Adt", "Adt")

masterNet.getEditor().addLibraryInstance(wslib,"WebServices.VisionInterface.WSNodes", "wslib")

masterNet.getEditor().addLibraryInstance(stdlib,"Vision.StandardNodes", "stdlib")

from WebServices.VisionInterface.WSNodes import addOpalServerAsCategory
try:
    addOpalServerAsCategory("http://kryptonite.nbcr.net/opal2", replace=False)
except:
    pass
try:
    ## saving node Directory_Containing_Input_PDB_Files ##
    from Vision.StandardNodes import DirBrowserNE
    Directory_Containing_Input_PDB_Files_0 = DirBrowserNE(constrkw={}, name='Directory_Containing_Input_PDB_Files', library=stdlib)
    masterNet.addNode(Directory_Containing_Input_PDB_Files_0,45,40)
    Directory_Containing_Input_PDB_Files_0.inputPortByName['directory'].widget.set(r"TrajQRClustering_0.1_input", run=False)
    apply(Directory_Containing_Input_PDB_Files_0.configure, (), {'paramPanelImmediate': 1})
except:
    print "WARNING: failed to restore DirBrowserNE named Directory_Containing_Input_PDB_Files in network masterNet"
    print_exc()
    Directory_Containing_Input_PDB_Files_0=None

try:
    ## saving node RMSD ##
    from Vision.StandardNodes import EntryNE
    RMSD_1 = EntryNE(constrkw={}, name='RMSD', library=stdlib)
    masterNet.addNode(RMSD_1,379,44)
    RMSD_1.inputPortByName['entry'].widget.set(r"0.5", run=False)
    apply(RMSD_1.configure, (), {'paramPanelImmediate': 1})
except:
    print "WARNING: failed to restore EntryNE named RMSD in network masterNet"
    print_exc()
    RMSD_1=None

try:
    ## saving node Output_Directory_Path ##
    from Vision.StandardNodes import DirBrowserNE
    Output_Directory_Path_2 = DirBrowserNE(constrkw={}, name='Output_Directory_Path', library=stdlib)
    masterNet.addNode(Output_Directory_Path_2,572,44)
    Output_Directory_Path_2.inputPortByName['directory'].widget.set(r"TrajQRClustering_0.1_output", run=False)
    apply(Output_Directory_Path_2.configure, (), {'paramPanelImmediate': 1})
except:
    print "WARNING: failed to restore DirBrowserNE named Output_Directory_Path in network masterNet"
    print_exc()
    Output_Directory_Path_2=None

try:
    ## saving node TrajQR2 ##
    from Adt.Macro.TrajQR import TrajQR
    TrajQR2_3 = TrajQR(constrkw={}, name='TrajQR2', library=Adt)
    masterNet.addNode(TrajQR2_3,297,173)
    apply(TrajQR2_3.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
    TrajQR_kryptonite_nbcr_net_7 = TrajQR2_3.macroNetwork.nodes[3]
    TrajQR_kryptonite_nbcr_net_7.inputPortByName['license'].widget.set(0, run=False)
    TrajQR_kryptonite_nbcr_net_7.inputPortByName['qh_filename'].widget.set(r"qh.tre", run=False)
    TrajQR_kryptonite_nbcr_net_7.inputPortByName['qr_filename'].widget.set(r"qr.out", run=False)
    TrajQR_kryptonite_nbcr_net_7.inputPortByName['localRun'].widget.set(0, run=False)
    TrajQR_kryptonite_nbcr_net_7.inputPortByName['execPath'].widget.set(r"", run=False)
    SelectOnExtension_8 = TrajQR2_3.macroNetwork.nodes[4]
    SelectOnExtension_8.inputPortByName['extension'].widget.set(r".out", run=False)
    Index_9 = TrajQR2_3.macroNetwork.nodes[5]
    apply(Index_9.inputPortByName['index'].widget.configure, (), {'max': 0, 'min': -1})
    Index_9.inputPortByName['index'].widget.set(0, run=False)

    ## saving connections for network TrajQR2 ##
    TrajQR2_3.macroNetwork.freeze()
    TrajQR2_3.macroNetwork.unfreeze()

    ## modifying MacroInputNode dynamic ports
    input_Ports_4 = TrajQR2_3.macroNetwork.ipNode
    input_Ports_4.outputPorts[1].configure(name='Make_Zip_File_input_directory')
    input_Ports_4.outputPorts[2].configure(name='TrajQR_kryptonite_nbcr_net_rmsd')
    input_Ports_4.outputPorts[3].configure(name='GetSelectedPDBs_pdb_out_dir')

    ## modifying MacroOutputNode dynamic ports
    output_Ports_5 = TrajQR2_3.macroNetwork.opNode
    output_Ports_5.inputPorts[1].configure(singleConnection='auto')
    output_Ports_5.inputPorts[1].configure(name='GetSelectedPDBs_pdb_out_dir')
    TrajQR2_3.inputPorts[0].configure(name='Make_Zip_File_input_directory')
    TrajQR2_3.inputPorts[0].configure(datatype='string')
    TrajQR2_3.inputPorts[1].configure(name='TrajQR_kryptonite_nbcr_net_rmsd')
    TrajQR2_3.inputPorts[1].configure(datatype='string')
    TrajQR2_3.inputPorts[2].configure(name='GetSelectedPDBs_pdb_out_dir')
    TrajQR2_3.inputPorts[2].configure(datatype='string')
    ## configure MacroNode input ports
    TrajQR2_3.outputPorts[0].configure(name='GetSelectedPDBs_pdb_out_dir')
    TrajQR2_3.outputPorts[0].configure(datatype='string')
    ## configure MacroNode output ports
    TrajQR2_3.shrink()
    apply(TrajQR2_3.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
except:
    print "WARNING: failed to restore TrajQR named TrajQR2 in network masterNet"
    print_exc()
    TrajQR2_3=None

try:
    ## saving node DPFTemplateBrowser ##
    from Adt.Input.DPFTemplateBrowser import DPFTemplateBrowser
    DPFTemplateBrowser_11 = DPFTemplateBrowser(constrkw={}, name='DPFTemplateBrowser', library=Adt)
    masterNet.addNode(DPFTemplateBrowser_11,823,165)
    DPFTemplateBrowser_11.inputPortByName['dpf_template_file'].widget.set(r"TrajQRClustering_0.1_input/GpfDpf/2HTY_A.dpf", run=False)
    apply(DPFTemplateBrowser_11.configure, (), {'paramPanelImmediate': 1})
except:
    print "WARNING: failed to restore DPFTemplateBrowser named DPFTemplateBrowser in network masterNet"
    print_exc()
    DPFTemplateBrowser_11=None

try:
    ## saving node GPFTemplateBrowser ##
    from Adt.Input.GPFTemplateBrowser import GPFTemplateBrowser
    GPFTemplateBrowser_12 = GPFTemplateBrowser(constrkw={}, name='GPFTemplateBrowser', library=Adt)
    masterNet.addNode(GPFTemplateBrowser_12,411,161)
    GPFTemplateBrowser_12.inputPortByName['gpf_template_file'].widget.set(r"TrajQRClustering_0.1_input/GpfDpf/2HTY_A.gpf", run=False)
    apply(GPFTemplateBrowser_12.configure, (), {'paramPanelImmediate': 1})
except:
    print "WARNING: failed to restore GPFTemplateBrowser named GPFTemplateBrowser in network masterNet"
    print_exc()
    GPFTemplateBrowser_12=None

try:
    ## saving node MakeGpfDpfCopies ##
    from Adt.Input.MakeGpfDpfCopies import MakeGpfDpfCopies
    MakeGpfDpfCopies_13 = MakeGpfDpfCopies(constrkw={}, name='MakeGpfDpfCopies', library=Adt)
    masterNet.addNode(MakeGpfDpfCopies_13,502,400)
    apply(MakeGpfDpfCopies_13.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
except:
    print "WARNING: failed to restore MakeGpfDpfCopies named MakeGpfDpfCopies in network masterNet"
    print_exc()
    MakeGpfDpfCopies_13=None

#masterNet.run()
masterNet.freeze()

## saving connections for network TrajQRClustering-0.1 ##
if Directory_Containing_Input_PDB_Files_0 is not None and TrajQR2_3 is not None:
    try:
        masterNet.connectNodes(
            Directory_Containing_Input_PDB_Files_0, TrajQR2_3, "directory", "Make_Zip_File_input_directory", blocking=True
            , splitratio=[0.53789406177278476, 0.25664890305372345])
    except:
        print "WARNING: failed to restore connection between Directory_Containing_Input_PDB_Files_0 and TrajQR2_3 in network masterNet"
if RMSD_1 is not None and TrajQR2_3 is not None:
    try:
        masterNet.connectNodes(
            RMSD_1, TrajQR2_3, "string", "TrajQR_kryptonite_nbcr_net_rmsd", blocking=True
            , splitratio=[0.34136199777603804, 0.27589115652596063])
    except:
        print "WARNING: failed to restore connection between RMSD_1 and TrajQR2_3 in network masterNet"
if Output_Directory_Path_2 is not None and TrajQR2_3 is not None:
    try:
        masterNet.connectNodes(
            Output_Directory_Path_2, TrajQR2_3, "directory", "GetSelectedPDBs_pdb_out_dir", blocking=True
            , splitratio=[0.48508950256597771, 0.43046378270767627])
    except:
        print "WARNING: failed to restore connection between Output_Directory_Path_2 and TrajQR2_3 in network masterNet"
if GPFTemplateBrowser_12 is not None and MakeGpfDpfCopies_13 is not None:
    try:
        masterNet.connectNodes(
            GPFTemplateBrowser_12, MakeGpfDpfCopies_13, "gpf_template", "gpf_file", blocking=True
            , splitratio=[0.28822475891698995, 0.59826911412993689])
    except:
        print "WARNING: failed to restore connection between GPFTemplateBrowser_12 and MakeGpfDpfCopies_13 in network masterNet"
if DPFTemplateBrowser_11 is not None and MakeGpfDpfCopies_13 is not None:
    try:
        masterNet.connectNodes(
            DPFTemplateBrowser_11, MakeGpfDpfCopies_13, "dpf_template", "dpf_file", blocking=True
            , splitratio=[0.35483561885882675, 0.39404164598930946])
    except:
        print "WARNING: failed to restore connection between DPFTemplateBrowser_11 and MakeGpfDpfCopies_13 in network masterNet"
if TrajQR2_3 is not None and MakeGpfDpfCopies_13 is not None:
    try:
        masterNet.connectNodes(
            TrajQR2_3, MakeGpfDpfCopies_13, "GetSelectedPDBs_pdb_out_dir", "struct_dir", blocking=True
            , splitratio=[0.42819979143655329, 0.42037477696550413])
    except:
        print "WARNING: failed to restore connection between TrajQR2_3 and MakeGpfDpfCopies_13 in network masterNet"
masterNet.runOnNewData.value = False

if __name__=='__main__':
    from sys import argv
    lNodePortValues = []
    if (len(argv) > 1) and argv[1].startswith('-'):
        lArgIndex = 2
    else:
        lArgIndex = 1
    while lArgIndex < len(argv) and argv[lArgIndex][-3:]!='.py':
        lNodePortValues.append(argv[lArgIndex])
        lArgIndex += 1
    masterNet.setNodePortValues(lNodePortValues)
    if '--help' in argv or '-h' in argv: # show help
        masterNet.helpForNetworkAsApplication()
    elif '-w' in argv: # run without Vision and exit
         # create communicator
        from NetworkEditor.net import Communicator
        masterNet.communicator = Communicator(masterNet)
        print 'Communicator listening on port:', masterNet.communicator.port

        import socket
        f = open(argv[0]+'.sock', 'w')
        f.write("%s %i"%(socket.gethostbyname(socket.gethostname()),
                         masterNet.communicator.port))
        f.close()

        masterNet.run()

    else: # stand alone application while vision is hidden
        if '-e' in argv: # run and exit
            masterNet.run()
        elif '-r' in argv or len(masterNet.userPanels) == 0: # no user panel => run
            masterNet.run()
            mainLoopVisionToRunNetworkAsApplication(masterNet.editor)
        else: # user panel
            mainLoopVisionToRunNetworkAsApplication(masterNet.editor)
