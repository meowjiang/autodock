########################################################################
#
#    Vision Macro - Python source code - file generated by vision
#    Thursday 22 July 2010 11:38:41 
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
# $Header: /home/cvs/CVSROOT/nbcr/src/roll/autodock/src/mgltools/patch-files/AutoDockTools/VisionInterface/Adt/Macro/Attic/TrajQR.py,v 1.1 2012/02/08 02:13:05 clem Exp $
#
# $Id: TrajQR.py,v 1.1 2012/02/08 02:13:05 clem Exp $
#

from NetworkEditor.macros import MacroNode
from NetworkEditor.macros import MacroNode
class TrajQR(MacroNode):
    '''
    This node runs Traj QR.

    Inputs:
       port 1: directory containing pdb files
       port 2: rmsd
       port 3: directory to copy the selected pdb files to

    Output:
       directory that containst he selected pdb files
    '''

    def __init__(self, constrkw={}, name='TrajQR', **kw):
        kw['name'] = name
        apply( MacroNode.__init__, (self,), kw)

    def beforeAddingToNetwork(self, net):
        MacroNode.beforeAddingToNetwork(self, net)
        from WebServices.VisionInterface.WSNodes import wslib
        from Vision.StandardNodes import stdlib
        net.getEditor().addLibraryInstance(wslib,"WebServices.VisionInterface.WSNodes", "wslib")
        from WebServices.VisionInterface.WSNodes import addOpalServerAsCategory
        try:
            addOpalServerAsCategory("http://kryptonite.nbcr.net/opal2", replace=False)
        except:
            pass

    def afterAddingToNetwork(self):
        masterNet = self.macroNetwork
        from NetworkEditor.macros import MacroNode
        MacroNode.afterAddingToNetwork(self)
        from WebServices.VisionInterface.WSNodes import wslib
        from Vision.StandardNodes import stdlib
        ## building macro network ##
        TrajQR_0 = self
        from traceback import print_exc
        from WebServices.VisionInterface.WSNodes import wslib
        from Vision.StandardNodes import stdlib
        masterNet.getEditor().addLibraryInstance(wslib,"WebServices.VisionInterface.WSNodes", "wslib")
        from WebServices.VisionInterface.WSNodes import addOpalServerAsCategory
        try:
            addOpalServerAsCategory("http://kryptonite.nbcr.net/opal2", replace=False)
        except:
            pass
        try:
            ## saving node input Ports ##
            input_Ports_1 = self.macroNetwork.ipNode
            apply(input_Ports_1.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
        except:
            print "WARNING: failed to restore MacroInputNode named input Ports in network self.macroNetwork"
            print_exc()
            input_Ports_1=None

        try:
            ## saving node output Ports ##
            output_Ports_2 = self.macroNetwork.opNode
            apply(output_Ports_2.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
            output_Ports_2.move(183, 405)
        except:
            print "WARNING: failed to restore MacroOutputNode named output Ports in network self.macroNetwork"
            print_exc()
            output_Ports_2=None

        try:
            ## saving node Make_Zip_File ##
            from Vision.StandardNodes import MakeZipFileNE
            Make_Zip_File_3 = MakeZipFileNE(constrkw={}, name='Make_Zip_File', library=stdlib)
            self.macroNetwork.addNode(Make_Zip_File_3,47,75)
            apply(Make_Zip_File_3.inputPortByName['input_directory'].configure, (), {'defaultValue': None})
            apply(Make_Zip_File_3.inputPortByName['output_directory'].configure, (), {'defaultValue': None})
            apply(Make_Zip_File_3.inputPortByName['output_name'].configure, (), {'defaultValue': None})
            apply(Make_Zip_File_3.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
        except:
            print "WARNING: failed to restore MakeZipFileNE named Make_Zip_File in network self.macroNetwork"
            print_exc()
            Make_Zip_File_3=None

        try:
            ## saving node TrajQR_kryptonite_nbcr_net ##
            from NetworkEditor.items import FunctionNode
            TrajQR_kryptonite_nbcr_net_4 = FunctionNode(functionOrString='TrajQR_kryptonite_nbcr_net', host="http://kryptonite.nbcr.net/opal2", namedArgs={'license': False, 'rmsd': '', 'qh_filename': 'qh.tre', 'qr_filename': 'qr.out', 'compressed_pdbs': '', 'localRun': False, 'execPath': ''}, constrkw={'functionOrString': "'TrajQR_kryptonite_nbcr_net'", 'host': '"http://kryptonite.nbcr.net/opal2"', 'namedArgs': {'license': False, 'rmsd': '', 'qh_filename': 'qh.tre', 'qr_filename': 'qr.out', 'compressed_pdbs': '', 'localRun': False, 'execPath': ''}}, name='TrajQR_kryptonite_nbcr_net', library=wslib)
            self.macroNetwork.addNode(TrajQR_kryptonite_nbcr_net_4,279,135)
            apply(TrajQR_kryptonite_nbcr_net_4.inputPortByName['license'].configure, (), {'defaultValue': None})
            apply(TrajQR_kryptonite_nbcr_net_4.inputPortByName['rmsd'].configure, (), {'defaultValue': None, 'required': True})
            apply(TrajQR_kryptonite_nbcr_net_4.inputPortByName['qh_filename'].configure, (), {'defaultValue': None})
            apply(TrajQR_kryptonite_nbcr_net_4.inputPortByName['qr_filename'].configure, (), {'defaultValue': None})
            apply(TrajQR_kryptonite_nbcr_net_4.inputPortByName['compressed_pdbs'].configure, (), {'defaultValue': None, 'required': True})
            apply(TrajQR_kryptonite_nbcr_net_4.inputPortByName['localRun'].configure, (), {'defaultValue': None})
            apply(TrajQR_kryptonite_nbcr_net_4.inputPortByName['execPath'].configure, (), {'defaultValue': None})
            TrajQR_kryptonite_nbcr_net_4.inputPortByName['license'].widget.set(0, run=False)
            TrajQR_kryptonite_nbcr_net_4.inputPortByName['rmsd'].rebindWidget()
            TrajQR_kryptonite_nbcr_net_4.inputPortByName['rmsd'].widget.set(r"", run=False)
            TrajQR_kryptonite_nbcr_net_4.inputPortByName['rmsd'].unbindWidget()
            TrajQR_kryptonite_nbcr_net_4.inputPortByName['qh_filename'].widget.set(r"qh.tre", run=False)
            TrajQR_kryptonite_nbcr_net_4.inputPortByName['qr_filename'].widget.set(r"qr.out", run=False)
            TrajQR_kryptonite_nbcr_net_4.inputPortByName['compressed_pdbs'].rebindWidget()
            TrajQR_kryptonite_nbcr_net_4.inputPortByName['compressed_pdbs'].widget.set(r"", run=False)
            TrajQR_kryptonite_nbcr_net_4.inputPortByName['compressed_pdbs'].unbindWidget()
            TrajQR_kryptonite_nbcr_net_4.inputPortByName['localRun'].widget.set(0, run=False)
            TrajQR_kryptonite_nbcr_net_4.inputPortByName['execPath'].widget.set(r"", run=False)
            apply(TrajQR_kryptonite_nbcr_net_4.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
        except:
            print "WARNING: failed to restore FunctionNode named TrajQR_kryptonite_nbcr_net in network self.macroNetwork"
            print_exc()
            TrajQR_kryptonite_nbcr_net_4=None

        try:
            ## saving node SelectOnExtension ##
            from Vision.StandardNodes import SelectOnExtension
            SelectOnExtension_5 = SelectOnExtension(constrkw={}, name='SelectOnExtension', library=stdlib)
            self.macroNetwork.addNode(SelectOnExtension_5,279,192)
            apply(SelectOnExtension_5.inputPortByName['filenames'].configure, (), {'defaultValue': None})
            apply(SelectOnExtension_5.inputPortByName['extension'].configure, (), {'defaultValue': None})
            SelectOnExtension_5.inputPortByName['extension'].widget.set(r".out", run=False)
            apply(SelectOnExtension_5.configure, (), {'paramPanelImmediate': 1})
        except:
            print "WARNING: failed to restore SelectOnExtension named SelectOnExtension in network self.macroNetwork"
            print_exc()
            SelectOnExtension_5=None

        try:
            ## saving node Index ##
            from Vision.StandardNodes import Index
            Index_6 = Index(constrkw={}, name='Index', library=stdlib)
            self.macroNetwork.addNode(Index_6,123,281)
            apply(Index_6.inputPortByName['data'].configure, (), {'datatype': 'list', 'defaultValue': None, 'originalDatatype': 'None'})
            apply(Index_6.inputPortByName['index'].configure, (), {'defaultValue': None})
            apply(Index_6.outputPortByName['data'].configure, (), {'datatype': 'string'})
            apply(Index_6.inputPortByName['index'].widget.configure, (), {'max': 0, 'min': -1})
            Index_6.inputPortByName['index'].widget.set(0, run=False)
            apply(Index_6.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
        except:
            print "WARNING: failed to restore Index named Index in network self.macroNetwork"
            print_exc()
            Index_6=None

        try:
            ## saving node GetSelectedPDBs ##
            from Vision.StandardNodes import Generic
            GetSelectedPDBs_7 = Generic(constrkw={}, name='GetSelectedPDBs', library=stdlib)
            self.macroNetwork.addNode(GetSelectedPDBs_7,200,346)
            apply(GetSelectedPDBs_7.addInputPort, (), {'singleConnection': True, 'name': 'trajqr_url', 'cast': True, 'datatype': 'string', 'defaultValue': None, 'required': True, 'height': 8, 'width': 12, 'shape': 'oval', 'color': 'white', 'originalDatatype': 'None'})
            apply(GetSelectedPDBs_7.addInputPort, (), {'singleConnection': True, 'name': 'pdb_in_dir', 'cast': True, 'datatype': 'string', 'defaultValue': None, 'required': True, 'height': 8, 'width': 12, 'shape': 'oval', 'color': 'white', 'originalDatatype': 'None'})
            apply(GetSelectedPDBs_7.addInputPort, (), {'singleConnection': True, 'name': 'pdb_out_dir', 'cast': True, 'datatype': 'string', 'defaultValue': None, 'required': True, 'height': 8, 'width': 12, 'shape': 'oval', 'color': 'white', 'originalDatatype': 'None'})
            apply(GetSelectedPDBs_7.addOutputPort, (), {'name': 'pdb_out_dir', 'datatype': 'string', 'height': 8, 'width': 12, 'shape': 'oval', 'color': 'white'})
            code = """def doit(self, trajqr_url, pdb_in_dir, pdb_out_dir):
        pdb_in_dir = os.path.abspath(pdb_in_dir)
        pdb_out_dir = os.path.abspath(pdb_out_dir)
        import urllib
        import shutil
        pdb_list = []

        f = urllib.urlopen(trajqr_url)

        for i in f.readlines():
            pdb_file = i.strip('''
''')+'''.pdb'''
            infile = pdb_in_dir + os.sep + pdb_file
            outfile = pdb_out_dir + os.sep + pdb_file
            shutil.copyfile(infile, outfile)
        
        f.close
	pass
## to ouput data on port pdb_list use
        self.outputData(pdb_out_dir=pdb_out_dir)


"""
            GetSelectedPDBs_7.configure(function=code)
            apply(GetSelectedPDBs_7.configure, (), {'paramPanelImmediate': 1, 'expanded': False})
        except:
            print "WARNING: failed to restore Generic named GetSelectedPDBs in network self.macroNetwork"
            print_exc()
            GetSelectedPDBs_7=None

        #self.macroNetwork.run()
        self.macroNetwork.freeze()

        ## saving connections for network TrajQR ##
        input_Ports_1 = self.macroNetwork.ipNode
        if input_Ports_1 is not None and Make_Zip_File_3 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_1, Make_Zip_File_3, "new", "input_directory", blocking=True
                    , splitratio=[0.67469172328672133, 0.50941480178765064])
            except:
                print "WARNING: failed to restore connection between input_Ports_1 and Make_Zip_File_3 in network self.macroNetwork"
        if input_Ports_1 is not None and TrajQR_kryptonite_nbcr_net_4 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_1, TrajQR_kryptonite_nbcr_net_4, "new", "rmsd", blocking=True
                    , splitratio=[0.45681934134493246, 0.33803410340720857])
            except:
                print "WARNING: failed to restore connection between input_Ports_1 and TrajQR_kryptonite_nbcr_net_4 in network self.macroNetwork"
        if Make_Zip_File_3 is not None and TrajQR_kryptonite_nbcr_net_4 is not None:
            try:
                self.macroNetwork.connectNodes(
                    Make_Zip_File_3, TrajQR_kryptonite_nbcr_net_4, "zipfile", "compressed_pdbs", blocking=True
                    , splitratio=[0.71081093868178202, 0.43908686250860129])
            except:
                print "WARNING: failed to restore connection between Make_Zip_File_3 and TrajQR_kryptonite_nbcr_net_4 in network self.macroNetwork"
        if TrajQR_kryptonite_nbcr_net_4 is not None and SelectOnExtension_5 is not None:
            try:
                self.macroNetwork.connectNodes(
                    TrajQR_kryptonite_nbcr_net_4, SelectOnExtension_5, "result", "filenames", blocking=True
                    , splitratio=[0.63533198718963335, 0.2560040659014205])
            except:
                print "WARNING: failed to restore connection between TrajQR_kryptonite_nbcr_net_4 and SelectOnExtension_5 in network self.macroNetwork"
        if SelectOnExtension_5 is not None and Index_6 is not None:
            try:
                self.macroNetwork.connectNodes(
                    SelectOnExtension_5, Index_6, "matching", "data", blocking=True
                    , splitratio=[0.65832290589891362, 0.21624347250969889])
            except:
                print "WARNING: failed to restore connection between SelectOnExtension_5 and Index_6 in network self.macroNetwork"
        if Index_6 is not None and GetSelectedPDBs_7 is not None:
            try:
                self.macroNetwork.connectNodes(
                    Index_6, GetSelectedPDBs_7, "data", "trajqr_url", blocking=True
                    , splitratio=[0.51754619993986595, 0.63949220525823236])
            except:
                print "WARNING: failed to restore connection between Index_6 and GetSelectedPDBs_7 in network self.macroNetwork"
        if input_Ports_1 is not None and GetSelectedPDBs_7 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_1, GetSelectedPDBs_7, "Make_Zip_File_input_directory", "pdb_in_dir", blocking=True
                    , splitratio=[0.7121964126696847, 0.42697952864467786])
            except:
                print "WARNING: failed to restore connection between input_Ports_1 and GetSelectedPDBs_7 in network self.macroNetwork"
        if input_Ports_1 is not None and GetSelectedPDBs_7 is not None:
            try:
                self.macroNetwork.connectNodes(
                    input_Ports_1, GetSelectedPDBs_7, "new", "pdb_out_dir", blocking=True
                    , splitratio=[0.62460995639428174, 0.60275185701976297])
            except:
                print "WARNING: failed to restore connection between input_Ports_1 and GetSelectedPDBs_7 in network self.macroNetwork"
        output_Ports_2 = self.macroNetwork.opNode
        if GetSelectedPDBs_7 is not None and output_Ports_2 is not None:
            try:
                self.macroNetwork.connectNodes(
                    GetSelectedPDBs_7, output_Ports_2, "pdb_out_dir", "new", blocking=True
                    , splitratio=[0.7431176169343523, 0.73697976585137526])
            except:
                print "WARNING: failed to restore connection between GetSelectedPDBs_7 and output_Ports_2 in network self.macroNetwork"
        self.macroNetwork.runOnNewData.value = True

        ## modifying MacroInputNode dynamic ports
        input_Ports_1 = self.macroNetwork.ipNode
        input_Ports_1.outputPorts[1].configure(name='Make_Zip_File_input_directory')
        input_Ports_1.outputPorts[2].configure(name='TrajQR_kryptonite_nbcr_net_rmsd')
        input_Ports_1.outputPorts[3].configure(name='GetSelectedPDBs_pdb_out_dir')

        ## modifying MacroOutputNode dynamic ports
        output_Ports_2 = self.macroNetwork.opNode
        output_Ports_2.inputPorts[1].configure(singleConnection='auto')
        output_Ports_2.inputPorts[1].configure(name='GetSelectedPDBs_pdb_out_dir')
        ## configure MacroNode input ports
        TrajQR_0.inputPorts[0].configure(name='Make_Zip_File_input_directory')
        TrajQR_0.inputPorts[0].configure(datatype='string')
        TrajQR_0.inputPorts[1].configure(name='TrajQR_kryptonite_nbcr_net_rmsd')
        TrajQR_0.inputPorts[1].configure(datatype='string')
        TrajQR_0.inputPorts[2].configure(name='GetSelectedPDBs_pdb_out_dir')
        TrajQR_0.inputPorts[2].configure(datatype='string')
        ## configure MacroNode output ports
        TrajQR_0.outputPorts[0].configure(name='GetSelectedPDBs_pdb_out_dir')
        TrajQR_0.outputPorts[0].configure(datatype='string')

        TrajQR_0.shrink()

        ## reset modifications ##
        TrajQR_0.resetTags()
        TrajQR_0.buildOriginalList()
