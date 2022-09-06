//Maya ASCII 2018ff07 scene
//Name: jen_bipedTemplate.ma
//Last modified: Mon, Jul 01, 2019 03:22:11 PM
//Codeset: 1252
requires maya "2018ff07";
requires "stereoCamera" "10.0";
requires -nodeType "ilrOptionsNode" -nodeType "ilrUIOptionsNode" -nodeType "ilrBakeLayerManager"
		 -nodeType "ilrBakeLayer" "Turtle" "2018.0.0";
requires "rpmaya" "2.0";
requires "CustomNode.py" "Unknown";
requires "elastikSolver" "0.991";
requires "Mayatomr" "2013.0 - 3.10.1.11 ";
requires "MayaExporter" "3.0";
requires "cryPoseReaderPlugin.py" "1.0";
requires "shaveNode" "1.1";
requires "ftb_displayNode.py" "Unknown";
requires "sk_rayShooter" "0.1";
requires "vrayformaya" "2.40.01";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2018";
fileInfo "version" "2018";
fileInfo "cutIdentifier" "201711281015-8e846c9074";
fileInfo "osv" "Microsoft Windows 8 Home Premium Edition, 64-bit  (Build 9200)\n";
createNode transform -s -n "persp";
	rename -uid "11A2202F-4F3A-8C31-BEDA-5EAC1AC081A3";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0.95932192773878344 77.480898648599691 207.83006102043339 ;
	setAttr ".r" -type "double3" -12.938352729713429 358.99999999982924 1.2425934254440825e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "5949EEA3-408C-4D7E-C42A-28AC206B135D";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 211.71715887774695;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -8.9929997383109139e-05 35.838505926088089 1.5655673013427713 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "2D60E3B6-4ED7-6CCC-506F-2FB0D80B94EB";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "EE867EC7-4E69-BF5A-D716-838BE4365CB9";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "294F62F1-43B7-6225-996D-E183EE2FDBB6";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -14.313685106448805 3.9712289316648146 1000.624498381474 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "EF98BAEB-4013-ED20-4F98-5EB6115C2249";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 991.37637714567359;
	setAttr ".ow" 40.73684520901174;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" -14.313685106448805 3.9712289316648146 9.2481212358005038 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "6F9CA6F3-48A1-0F80-92AE-C594801A169B";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.2425109498276 3.9712289316648146 9.2481212358007294 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "DBEFA1D5-4E58-C5E5-BBF2-7BA649397B17";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1014.5561960562765;
	setAttr ".ow" 4.216048642908504;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" -14.313685106448805 3.9712289316648146 9.2481212358005038 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "Points";
	rename -uid "BAD84280-4951-C485-0F4C-A0A95B5E05B1";
createNode joint -n "C_hip_01_point" -p "Points";
	rename -uid "C38533B5-44F9-3B7C-3F5A-5FAB962A0DE4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 0 31.0813 -1.591 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 111.65479999999998 -1.2608999999999999 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "C_spine_01_point" -p "C_hip_01_point";
	rename -uid "3F9EBCFF-44A8-DE13-8BFF-109FB3E9AB2A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 0 -0.047200000000000131 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 111.65479999999997 -1.2608999999999997 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "C_spine_02_point" -p "C_spine_01_point";
	rename -uid "F58B3AE5-4A65-6EB8-8497-E9AD1BC00E2A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0 0.85290000000000177 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 114.25639999999997 -1.2608999999999997 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "C_spine_03_point" -p "C_spine_02_point";
	rename -uid "831D46DC-45DE-BBCF-06C9-2489586794E4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0 0.88300000000000267 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 116.97299999999997 -1.2608999999999997 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "C_spine_04_point" -p "C_spine_03_point";
	rename -uid "C1333CE6-4CE3-5241-4F3B-87B12C41E1B1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0 0.90720000000000312 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 119.78199999999997 -1.2608999999999997 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "C_spine_05_point" -p "C_spine_04_point";
	rename -uid "CC6A3AD3-4EDE-5AA8-020C-73901003A43A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 0 0.89840000000000231 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 122.55719999999997 -1.2608999999999997 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "C_spine_06_point" -p "C_spine_05_point";
	rename -uid "9F27BDC3-4B71-D0F8-B0B5-3890BEAA0E38";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 0.85499999999999687 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 125.16689999999997 -1.2608999999999997 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "C_spine_07_point" -p "C_spine_06_point";
	rename -uid "71D60930-45A2-D922-5EE4-83B4EC563CFE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 0 0.91599999999999682 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 128.00949999999997 -1.2608999999999997 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "C_spine_08_endpoint" -p "C_spine_07_point";
	rename -uid "B9FC283A-4162-F149-9F9D-52A96B42FCC4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 0 0.92680000000000007 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 130.89349999999996 -1.2608999999999997 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "C_chest_01_point" -p "C_spine_08_endpoint";
	rename -uid "353F794C-43CD-6F10-E662-8D98469B15D3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 130.89349999999996 -1.2608999999999997 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "C_chest_01_endpoint" -p "C_chest_01_point";
	rename -uid "34A76D09-4C22-D935-1771-DE9D572769B0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0 5.9208 0.4196 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.96883815195128087 0.24769464128968713 0
		 0 -0.24769464128968713 0.96883815195128087 0 0 157.30109999999996 -0.1019000000000001 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "C_neck_01_point" -p "C_chest_01_endpoint";
	rename -uid "2AD94344-4B7E-ED70-3B37-34AA6B701DC8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0 0.3188999999999993 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.96883815195128087 0.24769464128968713 0
		 0 -0.24769464128968713 0.96883815195128087 0 0 158.48172617196781 0.19994068987560804 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "C_neck_01_endpoint" -p "C_neck_01_point";
	rename -uid "6CAF7CEA-4A94-1528-4246-9CBDE8E9B112";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0 5.009 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.96883815195128087 0.24769464128968713 0
		 0 -0.24769464128968713 0.96883815195128087 0 0 168.11914680468797 2.6638583646406389 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "C_head_01_point" -p "C_neck_01_endpoint";
	rename -uid "70A70525-46EC-4980-AF1F-E29BBF8D3867";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99779330908024089 0.066396629091414694 0
		 0 -0.066396629091414694 0.99779330908024089 0 0 168.11914680468797 2.6638583646406389 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "C_head_02_endpoint" -p "C_head_01_point";
	rename -uid "26BFDDE6-41A6-9607-0D89-8D866FDE3B6B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 0 23.764500000000005 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 0.99779330908024089 0.066396629091414694 0
		 0 -0.066396629091414694 0.99779330908024089 0 0 184.22103632997036 3.7353339666033518 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_clavicle_01_point" -p "C_chest_01_point";
	rename -uid "B35A1DDE-429C-3D4F-1760-32A8A07855AC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.2188 4.0949999999999989 0.7444 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.56059889711021116 9.1624296249588681 -14.859160400762644 ;
	setAttr ".bps" -type "matrix" 0.92038320164279075 -0.071210076365624875 -0.38447872133288169 0
		 0.06950386403779571 0.99741287598133543 -0.018351231851210795 0 0.38479081981978397 -0.0098325912476396101 0.92295143162128268 0
		 3.5308000000000002 152.46969999999999 4.5365000000000002 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_upperArm_01_point" -p "L_clavicle_01_point";
	rename -uid "56F9598E-404B-E841-5B42-D89E3EFB44BC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 4.1478999999999955 0 8.8817841970012523e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 6.3685369158661667 -5.8163230374802977 -26.194252788299515 ;
	setAttr ".bps" -type "matrix" 0.71453411608072037 -0.69921809272617752 -0.023131272362540922 0
		 0.69735827149685825 0.71449959689726739 -0.056407155650292695 0 0.055968188568662702 0.0241740529909449 0.99813985845187725 0
		 19.043674787048896 151.26946840487273 -1.9438119523214548 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_lowerArm_01_point" -p "L_upperArm_01_point";
	rename -uid "446F2F07-4FC4-6D28-8AA1-31BD4E78F4FF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 7.0260000000000176 2.1316282072803006e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -10.542114987012516 0 ;
	setAttr ".bps" -type "matrix" 0.70314434875333132 -0.66677788004824678 0.24697223223394843 0
		 0.69735827149685825 0.71449959689726739 -0.056407155650292695 0 -0.13885051671192075 0.21189050170313981 0.96737942364763185 0
		 40.783160908570018 129.99596769910653 -2.6475739745700535 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_lowerArm_02_endpoint" -p "L_lowerArm_01_point";
	rename -uid "F8E43078-416B-C95C-6253-00A11E4D392E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 9.1933999999999898 -7.1054273576010019e-15 1.3322676295501878e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.70314434875333132 -0.66677788004824678 0.24697223223394843 0
		 0.69735827149685825 0.71449959689726739 -0.056407155650292695 0 -0.13885051671192075 0.21189050170313981 0.96737942364763185 0
		 62.096379628329117 109.78520147134776 4.838445110404046 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_hand_01_point" -p "L_lowerArm_02_endpoint";
	rename -uid "C162D9D4-4D6F-27EA-808D-9DA915542103";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -1.2434497875801753e-14 -7.1054273576010019e-15 -4.9960036108132044e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.5939066143817241 -0.73860226721520716 0.31896962905297699 0
		 0.80437175917849646 0.53716456995211748 -0.25385093622881744 0 0.016155693415278699 0.40733391173914357 0.91313639611919939 0
		 62.096379628329125 109.78520147134779 4.8384451104040433 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerThumb_01_point" -p "L_hand_01_point";
	rename -uid "FFCED5C0-4B37-6AEF-4F6C-699D7D46426A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 0.809288752355803 0.11120986358788088 1.2116362656202901 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 55.118443625716957 -36.793116509910767 -19.86808822809747 ;
	setAttr ".bps" -type "matrix" 0.034215669834380416 -0.39190359663291968 0.9193698161697319 0
		 -0.158105515943812 0.90620183587919234 0.39217455103221893 0 -0.98682923232235309 -0.15877595408424769 -0.030955817526131579 0
		 61.800654227700853 108.48022610612543 9.277035430943446 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerThumb_02_point" -p "L_fingerThumb_01_point";
	rename -uid "1E4AE94C-4A08-51A8-687E-3EBA3DFBB2F9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 1.8985864008975746 -1.0658141036401503e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.23787859228018915 -0.48262199570977438 -8.2034673215737275 ;
	setAttr ".bps" -type "matrix" 0.077364582946845173 -0.63128944472241066 0.77167892175925812 0
		 -0.14206613790602968 0.75912043404634244 0.63525851357833674 0 -0.98682923232235309 -0.15877595408424769 -0.030955817526131579 0
		 61.909665351793215 107.23162124725297 12.206147665260197 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerThumb_03_point" -p "L_fingerThumb_02_point";
	rename -uid "93F6AD3C-4F7F-229A-C576-338F4A31D46A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 1.1650925987797063 3.5527136788005009e-15 3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -2.3136920031656865 ;
	setAttr ".bps" -type "matrix" 0.078082209175541137 -0.63512124245145074 0.76845570854616774 0
		 -0.14167298558420149 0.75591745831906976 0.63915378537883694 0 -0.98682923232235309 -0.15877595408424769 -0.030955817526131579 0
		 62.14134133188584 105.34116187608726 14.517017364360466 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerThumb_04_endpoint" -p "L_fingerThumb_03_point";
	rename -uid "BCC5C24A-4252-470B-C3C7-C086D8F2681E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 1.325100000000015 0 7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.078082209175541137 -0.63512124245145074 0.76845570854616774 0
		 -0.14167298558420149 0.75591745831906976 0.63915378537883694 0 -0.98682923232235309 -0.15877595408424769 -0.030955817526131579 0
		 62.379156316371741 103.40677310795286 16.857502915879529 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerRing_01_point" -p "L_hand_01_point";
	rename -uid "DFB158B6-4125-77D7-E1AD-35B09643EC9B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 1.4622000000000037 0.35430000000000206 -0.49619999999999853 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.42289765699957277 5.4282054033795966 5.8748493598623135 ;
	setAttr ".bps" -type "matrix" 0.44502365829092017 -0.8301252166375015 0.33592568860375582 0
		 0.89417860762666324 0.39139436904737523 -0.2173823027314975 0 0.0489751082102712 0.39711783211100982 0.91645996431663301 0
		 64.952983296691372 107.9232909697694 4.6175239796548322 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerRing_02_point" -p "L_fingerRing_01_point";
	rename -uid "716C6634-4A36-5172-8551-30B6E38D1A15";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 2.6852 7.1054273576010019e-15 -4.4408920985006262e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.19179176648383919 -5.9757635431475151 -22.814839298486312 ;
	setAttr ".bps" -type "matrix" 0.38783243019260377 -0.87117459908034034 0.30106614556955319 0
		 0.91915385187445187 0.34113294766463303 -0.19693782928121403 0 0.068863652787642921 0.35310498429623871 0.93304590851141744 0
		 67.903490151160142 102.41956078346276 6.8447112950977358 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerRing_03_point" -p "L_fingerRing_02_point";
	rename -uid "057107D3-4EFD-5DC6-3D50-368E3A1D7A09";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 1.5938999999999997 -1.4210854715202004e-14 6.591949208711867e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -19.145663761716786 ;
	setAttr ".bps" -type "matrix" 0.1986567576007307 -0.92138933071003293 0.33403172590830632 0
		 0.9776468124963672 0.16235323008449937 -0.13359692622520214 0 0.068863652787642921 0.35310498429623871 0.93304590851141744 0
		 69.595835743548605 98.618103302915813 8.1584435279050549 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerRing_04_point" -p "L_fingerRing_03_point";
	rename -uid "5D403923-41B2-60D4-893C-2AB1E78A3FF1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 1.0711000000000013 1.0658141036401503e-14 -1.1102230246251565e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -4.0536635552561426 ;
	setAttr ".bps" -type "matrix" 0.13627725829452575 -0.92982855998983927 0.34182942807626865 0
		 0.98827440834844527 0.10361331522721805 -0.1121515702571973 0 0.068863652787642921 0.35310498429623871 0.93304590851141744 0
		 70.059957526331232 96.465461409577955 8.9388418491446089 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerRing_05_endpoint" -p "L_fingerRing_04_point";
	rename -uid "00044555-4EC3-C3E1-4DB8-C4A3063C9864";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 1.1170000000000009 0 -8.0491169285323849e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.13627725829452575 -0.92982855998983927 0.34182942807626865 0
		 0.98827440834844527 0.10361331522721805 -0.1121515702571973 0 0.068863652787642921 0.35310498429623871 0.93304590851141744 0
		 70.415395871415001 94.040282559412447 9.8304013634531451 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerPinky_01_point" -p "L_hand_01_point";
	rename -uid "041B7419-4221-0466-C147-7E8A074E9C7C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 1.3710000000000049 0.24900000000000944 -1.2902999999999993 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.5745713021451585 9.4909048536323422 4.3850414077214621 ;
	setAttr ".bps" -type "matrix" 0.40798064724639849 -0.89887936776129185 0.1598989483563602 0
		 0.89514247352714638 0.35936181178820792 -0.26377839243576828 0 0.17964337883738254 0.25074881942166105 0.95123776522935222 0
		 64.404861384243503 107.52218719186229 3.6167298557496688 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerPinky_02_point" -p "L_fingerPinky_01_point";
	rename -uid "7F7740F6-4036-5F20-ED9D-368F0B10AED5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 2.5603000000000065 -2.1316282072803006e-14 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.92132373809430113 -9.392160709686399 -21.684190186528685 ;
	setAttr ".bps" -type "matrix" 0.32091604996658324 -0.93362417006291643 0.15924445970951659 0
		 0.88339126468981632 0.23443679069863355 -0.4057822872386761 0 0.34151539107860385 0.27089721342467782 0.89998996517470842 0
		 67.045271335157452 101.70472981164797 4.6515798596171889 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerPinky_03_point" -p "L_fingerPinky_02_point";
	rename -uid "7973C942-4758-C0A3-B33A-62B9780EDDDB";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 1.095399999999989 7.1054273576010019e-15 1.3322676295501878e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -9.7934351274093991 ;
	setAttr ".bps" -type "matrix" 0.23520107046132746 -0.95172735344683812 0.19721942387838678 0
		 0.90997126004631224 0.14432513453941986 -0.38874485389507668 0 0.34151539107860385 0.27089721342467782 0.89998996517470842 0
		 68.0696353666508 98.72460146080715 5.159888175009975 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerPinky_04_point" -p "L_fingerPinky_03_point";
	rename -uid "0FE19EB2-4183-C18E-62E5-C1B9384616B4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.9634999999999998 7.1054273576010019e-15 1.7763568394002505e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -6.1478835646679055 ;
	setAttr ".bps" -type "matrix" 0.13639498190840732 -0.96171027321309988 0.23771781444938025 0
		 0.92992668881295848 0.0415698226497212 -0.36538788058477983 0 0.34151539107860385 0.27089721342467782 0.89998996517470842 0
		 68.534674923166889 96.842846137572096 5.549830419902321 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerPinky_05_endpoint" -p "L_fingerPinky_04_point";
	rename -uid "A78B7544-4E11-7AD8-256A-DD87C94C7A35";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.93989999999999796 -1.7763568394002505e-14 8.8817841970012523e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.13639498190840732 -0.96171027321309988 0.23771781444938025 0
		 0.92992668881295848 0.0415698226497212 -0.36538788058477983 0 0.34151539107860385 0.27089721342467782 0.89998996517470842 0
		 68.798135470221197 94.985206573833665 6.0090061502927483 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_handEnd_01_endpoint" -p "L_hand_01_point";
	rename -uid "90B73F96-4429-3A06-E25D-949B3BC98017";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 4.1395000000000062 0 9.9920072216264089e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.5939066143817241 -0.73860226721520716 0.31896962905297699 0
		 0.80437175917849646 0.53716456995211748 -0.25385093622881744 0 0.016155693415278699 0.40733391173914357 0.91313639611919939 0
		 68.035505162807809 102.39910493896902 8.0281732978967106 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerMiddle_01_point" -p "L_hand_01_point";
	rename -uid "FDBC85A3-492F-B012-D172-9AB8DA6484CF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 1.487300000000003 0.34890000000000043 0.39200000000000246 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.24189155880517257 2.168104233795578 6.3676067733941935 ;
	setAttr ".bps" -type "matrix" 0.44240884535745983 -0.79968133071715908 0.40593618076233728 0
		 0.89153106858919962 0.44122509101650526 -0.102434236452839 0 -0.097194481786152323 0.40722252928823865 0.90814263436445442 0
		 65.024896941696994 108.64497371087407 6.4544591170109893 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerMiddle_02_point" -p "L_fingerMiddle_01_point";
	rename -uid "0119B87A-44AB-32B5-FAE9-D79BE6BCC75C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 2.8422000000000076 -7.1054273576010019e-15 -1.4432899320127035e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.035050096736816021 -2.3555326398906105 -23.525762458833373 ;
	setAttr ".bps" -type "matrix" 0.42275103695428745 -0.80414126788699725 0.41789757361722923 0
		 0.90055327418381204 0.42436884534105884 -0.094418660553473172 0 -0.10141676937711175 0.41625461485128212 0.90357442112098363 0
		 68.145162287118595 103.00490125345905 9.3174864063096514 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerMiddle_03_point" -p "L_fingerMiddle_02_point";
	rename -uid "409BC219-457E-A121-F91E-03B11245F875";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 1.6595999999999762 1.0658141036401503e-14 1.9428902930940239e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.1793069110865137 0.099040773337224081 -12.678555138006381 ;
	setAttr ".bps" -type "matrix" 0.34694282996047571 -0.83643774782613478 0.4242670936456891 0
		 0.9323868894552978 0.35651646473417486 -0.05958773989101776 0 -0.10141676937711175 0.41625461485128212 0.90357442112098363 0
		 69.87404492784691 99.716285124308371 11.026520323374697 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerMiddle_04_point" -p "L_fingerMiddle_03_point";
	rename -uid "EFEF572A-4C10-F5B4-5AB8-CDAEED719DD4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 1.1619000000000099 0 -1.0824674490095276e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -7.6574777984232982 ;
	setAttr ".bps" -type "matrix" 0.32478294014039705 -0.84463967029567988 0.42555830288758861 0
		 0.94033540860847542 0.33662430538779581 -0.04953177100927128 0 -0.10141676937711175 0.41625461485128212 0.90357442112098363 0
		 70.838476606570978 97.391155472901261 12.205897990290993 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerMiddle_05_endpoint" -p "L_fingerMiddle_04_point";
	rename -uid "D933D550-4A84-E58C-9C32-17A5868ACC87";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 1.0994000000000028 -1.0658141036401503e-14 1.0269562977782698e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.32478294014039705 -0.84463967029567988 0.42555830288758861 0
		 0.94033540860847542 0.33662430538779581 -0.04953177100927128 0 -0.10141676937711175 0.41625461485128212 0.90357442112098363 0
		 71.663750057467766 95.244926070679952 13.287241637928338 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerIndex_01_point" -p "L_hand_01_point";
	rename -uid "A72EF5D4-46E5-1ABB-3DA1-BEBC7BECC526";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" 1.5316000000000036 0.14900000000000091 1.1833000000000018 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.33234974322657634 -3.0785935847365558 6.1645186010763933 ;
	setAttr ".bps" -type "matrix" 0.46060384413781436 -0.73439291644218296 0.49850891972462535 0
		 0.79079952408287502 0.59458756291652348 0.14526438908172667 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 64.328752580308674 109.10393549685642 8.2274647732668171 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerIndex_02_point" -p "L_fingerIndex_01_point";
	rename -uid "BAD860BC-47E2-6C4B-2DE0-3D8195125B15";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 2.8344999999999971 0 -1.1102230246251565e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 2.597036252680458 -20.31453840211222 ;
	setAttr ".bps" -type "matrix" 0.40640166856417559 -0.7727019017824277 0.48761609363317121 0
		 0.81997406807318451 0.5438741551841616 0.17844727795689863 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 67.556894621948544 103.95694274197136 11.721264537156857 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerIndex_03_point" -p "L_fingerIndex_02_point";
	rename -uid "34D8367F-4D3F-474E-0DF7-B5A85740B09E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 1.5501000000000005 0 -5.5511151231257827e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -20.033938689993928 ;
	setAttr ".bps" -type "matrix" 0.3797825280139645 -0.78981722230580553 0.48161601589281089 0
		 0.83263738802647802 0.51870616060020713 0.19405900910763185 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 69.188597321233672 100.85454460631493 13.679043153094021 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerIndex_04_point" -p "L_fingerIndex_03_point";
	rename -uid "B34A7D29-405B-EE39-89B6-6191EF951B3F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 0.95890000000000342 -7.1054273576010019e-15 2.55351295663786e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -7.6711261710933361 ;
	setAttr ".bps" -type "matrix" 0.30686295657882046 -0.83145069712004416 0.46316828921926201 0
		 0.86218032592024407 0.44895107077949914 0.23470837573892045 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 70.034904706660001 99.094515908128727 14.752276282909548 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_fingerIndex_05_endpoint" -p "L_fingerIndex_04_point";
	rename -uid "1CCE8EE0-4528-FD4C-F71B-E2AE5717CB60";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 0.99830000000001107 1.0658141036401503e-14 -1.8873791418627661e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.30686295657882046 -0.83145069712004416 0.46316828921926201 0
		 0.86218032592024407 0.44895107077949914 0.23470837573892045 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 70.69616369179171 97.302822800904707 15.750357629348152 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_clavicle_01_point" -p "C_chest_01_point";
	rename -uid "B3C8F244-4262-06A6-585D-2AB01444D8EE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.2188 4.0949999999999989 0.7444 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 179.43940110288872 -9.162429624958877 14.859160400762663 ;
	setAttr ".bps" -type "matrix" 0.92038320164279075 -0.071210076365624875 -0.38447872133288169 0
		 0.06950386403779571 0.99741287598133543 -0.018351231851210795 0 0.38479081981978397 -0.0098325912476396101 0.92295143162128268 0
		 3.5308000000000002 152.46969999999999 4.5365000000000002 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_upperArm_01_point" -p "R_clavicle_01_point";
	rename -uid "58FC8DD0-4C50-7750-05E9-53926093A86F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -4.1479000000000044 1.4210854715202004e-14 -8.8817841970012523e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 6.3685369158672769 -5.8163230374798269 -26.194252788299593 ;
	setAttr ".bps" -type "matrix" 0.71453411608072037 -0.69921809272617752 -0.023131272362540922 0
		 0.69735827149685825 0.71449959689726739 -0.056407155650292695 0 0.055968188568662702 0.0241740529909449 0.99813985845187725 0
		 19.043674787048896 151.26946840487273 -1.9438119523214548 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_lowerArm_01_point" -p "R_upperArm_01_point";
	rename -uid "56DF63F5-4360-64AF-533A-48B2D2537957";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -7.0259999999999749 -1.4210854715202004e-14 8.8817841970012523e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.4787793311206573e-06 -10.542114987012527 2.5476900411344951e-14 ;
	setAttr ".bps" -type "matrix" 0.70314434875333132 -0.66677788004824678 0.24697223223394843 0
		 0.69735827149685825 0.71449959689726739 -0.056407155650292695 0 -0.13885051671192075 0.21189050170313981 0.96737942364763185 0
		 40.783160908570018 129.99596769910653 -2.6475739745700535 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_lowerArm_02_endpoint" -p "R_lowerArm_01_point";
	rename -uid "55BC8686-4C65-A924-3876-8CA6BC69E1EA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -9.1934000000000111 7.1054273576010019e-15 2.2204460492503131e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.9090959104164228e-06 7.4017691290211787e-22 -4.2390443486105665e-22 ;
	setAttr ".bps" -type "matrix" 0.70314434875333132 -0.66677788004824678 0.24697223223394843 0
		 0.69735827149685825 0.71449959689726739 -0.056407155650292695 0 -0.13885051671192075 0.21189050170313981 0.96737942364763185 0
		 62.096379628329117 109.78520147134776 4.838445110404046 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_hand_01_point" -p "R_lowerArm_02_endpoint";
	rename -uid "0C5CE9A6-41DF-7472-FA1D-D8B15D58FE1C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -6.2172489379008766e-15 1.4210854715202004e-14 1.1102230246251565e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 3.721513044668941e-06 1.2782476470498636e-21 -9.2963458892993452e-22 ;
	setAttr ".bps" -type "matrix" 0.5939066143817241 -0.73860226721520716 0.31896962905297699 0
		 0.80437175917849646 0.53716456995211748 -0.25385093622881744 0 0.016155693415278699 0.40733391173914357 0.91313639611919939 0
		 62.096379628329125 109.78520147134779 4.8384451104040433 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerThumb_01_point" -p "R_hand_01_point";
	rename -uid "2A73047B-40F2-795A-967D-8181E70D43C3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -0.80899999999999039 -0.11100000000002552 -1.2119999999999984 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 55.118377961512309 -36.793065502362431 -19.867987531602147 ;
	setAttr ".bps" -type "matrix" 0.034215669834380416 -0.39190359663291968 0.9193698161697319 0
		 -0.158105515943812 0.90620183587919234 0.39217455103221893 0 -0.98682923232235309 -0.15877595408424769 -0.030955817526131579 0
		 61.800654227700853 108.48022610612543 9.277035430943446 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerThumb_02_point" -p "R_fingerThumb_01_point";
	rename -uid "1DB52CEA-4ABA-55D7-AE3F-D099A770F385";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -1.8990000000000116 -3.5527136788005009e-15 -3.5527136788005009e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.2378785922819637 -0.48262199570977893 -8.2034673215737204 ;
	setAttr ".bps" -type "matrix" 0.077364582946845173 -0.63128944472241066 0.77167892175925812 0
		 -0.14206613790602968 0.75912043404634244 0.63525851357833674 0 -0.98682923232235309 -0.15877595408424769 -0.030955817526131579 0
		 61.909665351793215 107.23162124725297 12.206147665260197 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerThumb_03_point" -p "R_fingerThumb_02_point";
	rename -uid "99D4D3F8-431F-3F71-2D5D-25A2E6F94851";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.1649999999999938 1.4210854715202004e-14 -0.00010000000000331966 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.2074182682485221e-06 7.3152757078274286e-14 -2.3136920031656492 ;
	setAttr ".bps" -type "matrix" 0.078082209175541137 -0.63512124245145074 0.76845570854616774 0
		 -0.14167298558420149 0.75591745831906976 0.63915378537883694 0 -0.98682923232235309 -0.15877595408424769 -0.030955817526131579 0
		 62.14134133188584 105.34116187608726 14.517017364360466 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerThumb_04_endpoint" -p "R_fingerThumb_03_point";
	rename -uid "E1FA8B7C-46EA-4169-D4EF-81AB244770C5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -1.3251000000000044 0 7.1054273576010019e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.078082209175541137 -0.63512124245145074 0.76845570854616774 0
		 -0.14167298558420149 0.75591745831906976 0.63915378537883694 0 -0.98682923232235309 -0.15877595408424769 -0.030955817526131579 0
		 62.379156316371741 103.40677310795286 16.857502915879529 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerRing_01_point" -p "R_hand_01_point";
	rename -uid "9646E8A7-4E26-9F48-E493-99BC79CC6305";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -1.4620999999999897 -0.35440000000001959 0.49620000000000009 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.42289055309298307 5.4282061310673688 5.8748486878441986 ;
	setAttr ".bps" -type "matrix" 0.44502365829092017 -0.8301252166375015 0.33592568860375582 0
		 0.89417860762666324 0.39139436904737523 -0.2173823027314975 0 0.0489751082102712 0.39711783211100982 0.91645996431663301 0
		 64.952983296691372 107.9232909697694 4.6175239796548322 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerRing_02_point" -p "R_fingerRing_01_point";
	rename -uid "C3DF5ED1-46E0-53B2-6E19-8D898DDC1C85";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -2.6851999999999951 0.00010000000000331966 -6.6613381477509392e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.1917917664837088 -5.9757635431473615 -22.81483929848639 ;
	setAttr ".bps" -type "matrix" 0.38783243019260377 -0.87117459908034034 0.30106614556955319 0
		 0.91915385187445187 0.34113294766463303 -0.19693782928121403 0 0.068863652787642921 0.35310498429623871 0.93304590851141744 0
		 67.903490151160142 102.41956078346276 6.8447112950977358 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerRing_03_point" -p "R_fingerRing_02_point";
	rename -uid "8AC946F8-4614-2C70-2DB6-08BCBD271A53";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.5939000000000032 -0.00010000000002463594 3.677613769070831e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.4885083478614671e-14 8.8260392410612552e-14 -19.14566376171679 ;
	setAttr ".bps" -type "matrix" 0.1986567576007307 -0.92138933071003293 0.33403172590830632 0
		 0.9776468124963672 0.16235323008449937 -0.13359692622520214 0 0.068863652787642921 0.35310498429623871 0.93304590851141744 0
		 69.595835743548605 98.618103302915813 8.1584435279050549 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerRing_04_point" -p "R_fingerRing_03_point";
	rename -uid "1FEF7C08-4527-2300-1A1F-BCB1F3FA94F0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -1.0711000000000155 1.7763568394002505e-14 8.6736173798840355e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.7075472886480511e-06 1.0893399614579145e-13 -4.0536635552560938 ;
	setAttr ".bps" -type "matrix" 0.13627725829452575 -0.92982855998983927 0.34182942807626865 0
		 0.98827440834844527 0.10361331522721805 -0.1121515702571973 0 0.068863652787642921 0.35310498429623871 0.93304590851141744 0
		 70.059957526331232 96.465461409577955 8.9388418491446089 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerRing_05_endpoint" -p "R_fingerRing_04_point";
	rename -uid "0EAF82BC-4512-477F-489B-3A9F7B52902A";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -1.1169999999999973 7.1054273576010019e-15 -2.2204460492503131e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.258872743922551e-06 -2.3197635074460622e-21 -4.2006530334797792e-21 ;
	setAttr ".bps" -type "matrix" 0.13627725829452575 -0.92982855998983927 0.34182942807626865 0
		 0.98827440834844527 0.10361331522721805 -0.1121515702571973 0 0.068863652787642921 0.35310498429623871 0.93304590851141744 0
		 70.415395871415001 94.040282559412447 9.8304013634531451 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerPinky_01_point" -p "R_hand_01_point";
	rename -uid "CBC60DAF-4285-82CE-8F2E-D1ACE2B0345E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -1.3709999999999889 -0.24910000000001986 1.2903 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.5745641151968045 9.4909053972070048 4.3850402226571212 ;
	setAttr ".bps" -type "matrix" 0.40798064724639849 -0.89887936776129185 0.1598989483563602 0
		 0.89514247352714638 0.35936181178820792 -0.26377839243576828 0 0.17964337883738254 0.25074881942166105 0.95123776522935222 0
		 64.404861384243503 107.52218719186229 3.6167298557496688 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerPinky_02_point" -p "R_fingerPinky_01_point";
	rename -uid "830C64A0-4F9A-9E8C-EDFA-0985E19693D6";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -2.560400000000004 7.1054273576010019e-15 -8.8817841970012523e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.9213237380892747 -9.3921607096884738 -21.68419018652779 ;
	setAttr ".bps" -type "matrix" 0.32091604996658324 -0.93362417006291643 0.15924445970951659 0
		 0.88339126468981632 0.23443679069863355 -0.4057822872386761 0 0.34151539107860385 0.27089721342467782 0.89998996517470842 0
		 67.045271335157452 101.70472981164797 4.6515798596171889 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerPinky_03_point" -p "R_fingerPinky_02_point";
	rename -uid "639F7AE6-4673-A650-0B92-BB84AD48D313";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.0953999999999997 -7.1054273576010019e-15 -1.3322676295501878e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 4.9047510909229157e-15 -5.7249984266343195e-14 -9.7934351274093991 ;
	setAttr ".bps" -type "matrix" 0.23520107046132746 -0.95172735344683812 0.19721942387838678 0
		 0.90997126004631224 0.14432513453941986 -0.38874485389507668 0 0.34151539107860385 0.27089721342467782 0.89998996517470842 0
		 68.0696353666508 98.72460146080715 5.159888175009975 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerPinky_04_point" -p "R_fingerPinky_03_point";
	rename -uid "9A0812B5-4A9D-D1DD-9C86-ACB274B0A872";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.96340000000000359 7.1054273576010019e-15 8.8817841970012523e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.2074182745935887e-06 -9.0645808172891926e-14 -6.1478835646679384 ;
	setAttr ".bps" -type "matrix" 0.13639498190840732 -0.96171027321309988 0.23771781444938025 0
		 0.92992668881295848 0.0415698226497212 -0.36538788058477983 0 0.34151539107860385 0.27089721342467782 0.89998996517470842 0
		 68.534674923166889 96.842846137572096 5.549830419902321 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerPinky_05_endpoint" -p "R_fingerPinky_04_point";
	rename -uid "D58D3CBB-4246-0C8A-43EC-3182E6603ABF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -0.93990000000000151 -0.00010000000001042508 4.4408920985006262e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.7075472925031877e-06 3.3471978772705054e-22 2.7251525896619564e-21 ;
	setAttr ".bps" -type "matrix" 0.13639498190840732 -0.96171027321309988 0.23771781444938025 0
		 0.92992668881295848 0.0415698226497212 -0.36538788058477983 0 0.34151539107860385 0.27089721342467782 0.89998996517470842 0
		 68.798135470221197 94.985206573833665 6.0090061502927483 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_handEnd_01_endpoint" -p "R_hand_01_point";
	rename -uid "7121D512-46D6-E8FA-3C5F-6DB4B2A0FA58";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -4.1394999999999911 -2.1316282072803006e-14 1.1102230246251565e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 7.143182815269534e-06 2.9367730319440227e-21 -1.7843681738225026e-21 ;
	setAttr ".bps" -type "matrix" 0.5939066143817241 -0.73860226721520716 0.31896962905297699 0
		 0.80437175917849646 0.53716456995211748 -0.25385093622881744 0 0.016155693415278699 0.40733391173914357 0.91313639611919939 0
		 68.035505162807809 102.39910493896902 8.0281732978967106 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerMiddle_01_point" -p "R_hand_01_point";
	rename -uid "2EB02F6B-4ABF-E6E9-43A0-B6AC31C8859D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -1.487199999999989 -0.34890000000002175 -0.39199999999999902 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.24188448822161357 2.1681050222769982 6.3676065059028968 ;
	setAttr ".bps" -type "matrix" 0.44240884535745983 -0.79968133071715908 0.40593618076233728 0
		 0.89153106858919962 0.44122509101650526 -0.102434236452839 0 -0.097194481786152323 0.40722252928823865 0.90814263436445442 0
		 65.024896941696994 108.64497371087407 6.4544591170109893 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerMiddle_02_point" -p "R_fingerMiddle_01_point";
	rename -uid "E124F27B-474C-81E4-E996-A9AD3C77DFA8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -2.8421999999999992 7.1054273576010019e-15 -1.8318679906315083e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.035050096726887907 -2.355532639893438 -23.525762458833064 ;
	setAttr ".bps" -type "matrix" 0.42275103695428745 -0.80414126788699725 0.41789757361722923 0
		 0.90055327418381204 0.42436884534105884 -0.094418660553473172 0 -0.10141676937711175 0.41625461485128212 0.90357442112098363 0
		 68.145162287118595 103.00490125345905 9.3174864063096514 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerMiddle_03_point" -p "R_fingerMiddle_02_point";
	rename -uid "98B4786E-4443-4019-2DDB-36AD1521A290";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.6597000000000062 -1.0658141036401503e-14 1.1657341758564144e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0.17930691109973937 0.099040773337972704 -12.678555138006381 ;
	setAttr ".bps" -type "matrix" 0.34694282996047571 -0.83643774782613478 0.4242670936456891 0
		 0.9323868894552978 0.35651646473417486 -0.05958773989101776 0 -0.10141676937711175 0.41625461485128212 0.90357442112098363 0
		 69.87404492784691 99.716285124308371 11.026520323374697 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerMiddle_04_point" -p "R_fingerMiddle_03_point";
	rename -uid "54182D69-4D30-C4CA-1248-69A601CDB24E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -1.1618999999999993 3.5527136788005009e-15 4.9960036108132044e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.9090959986446664e-06 -1.3183399151822644e-12 -7.6574777984233 ;
	setAttr ".bps" -type "matrix" 0.32478294014039705 -0.84463967029567988 0.42555830288758861 0
		 0.94033540860847542 0.33662430538779581 -0.04953177100927128 0 -0.10141676937711175 0.41625461485128212 0.90357442112098363 0
		 70.838476606570978 97.391155472901261 12.205897990290993 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerMiddle_05_endpoint" -p "R_fingerMiddle_04_point";
	rename -uid "D30B3E3B-4332-8DC0-9263-C39E546CD380";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -1.0994999999999919 3.5527136788005009e-15 1.6653345369377348e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.4148365394514671e-06 5.0687673828431153e-22 5.559738530280351e-20 ;
	setAttr ".bps" -type "matrix" 0.32478294014039705 -0.84463967029567988 0.42555830288758861 0
		 0.94033540860847542 0.33662430538779581 -0.04953177100927128 0 -0.10141676937711175 0.41625461485128212 0.90357442112098363 0
		 71.663750057467766 95.244926070679952 13.287241637928338 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerIndex_01_point" -p "R_hand_01_point";
	rename -uid "030AE7F3-4C14-77D9-36B1-A295C7A63EF8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 7;
	setAttr ".t" -type "double3" -1.5315999999999859 -0.14900000000002223 -1.1832999999999996 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -0.33235682172808168 -3.0785928213041394 6.1645189812321721 ;
	setAttr ".bps" -type "matrix" 0.46060384413781436 -0.73439291644218296 0.49850891972462535 0
		 0.79079952408287502 0.59458756291652348 0.14526438908172667 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 64.328752580308674 109.10393549685642 8.2274647732668171 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerIndex_02_point" -p "R_fingerIndex_01_point";
	rename -uid "B434BCA8-4B34-B94E-6500-6C90627AE4F1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" -2.834500000000006 0 4.4408920985006262e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 7.3054848555470906e-12 2.597036252682658 -20.314538402111921 ;
	setAttr ".bps" -type "matrix" 0.40640166856417559 -0.7727019017824277 0.48761609363317121 0
		 0.81997406807318451 0.5438741551841616 0.17844727795689863 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 67.556894621948544 103.95694274197136 11.721264537156857 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerIndex_03_point" -p "R_fingerIndex_02_point";
	rename -uid "D17F3C22-4ED6-BAE5-A53D-E6BF33E4DBFA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -1.550100000000004 -7.1054273576010019e-15 -4.4408920985006262e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -3.6347743779301234e-13 2.0578188789068944e-12 -20.033938689993914 ;
	setAttr ".bps" -type "matrix" 0.3797825280139645 -0.78981722230580553 0.48161601589281089 0
		 0.83263738802647802 0.51870616060020713 0.19405900910763185 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 69.188597321233672 100.85454460631493 13.679043153094021 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerIndex_04_point" -p "R_fingerIndex_03_point";
	rename -uid "C92DA3F9-4396-D82A-6F0B-C7ACA6330A4C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -0.95900000000002095 7.1054273576010019e-15 6.6613381477509392e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 8.537734590311336e-07 2.7925270100761495e-12 -7.6711261710933343 ;
	setAttr ".bps" -type "matrix" 0.30686295657882046 -0.83145069712004416 0.46316828921926201 0
		 0.86218032592024407 0.44895107077949914 0.23470837573892045 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 70.034904706660001 99.094515908128727 14.752276282909548 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_fingerIndex_05_endpoint" -p "R_fingerIndex_04_point";
	rename -uid "44DA067C-432A-46EF-BE21-E79400080160";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -0.99829999999997909 3.5527136788005009e-15 -8.8817841970012523e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.30686295657882046 -0.83145069712004416 0.46316828921926201 0
		 0.86218032592024407 0.44895107077949914 0.23470837573892045 0 -0.40308834202413485 0.32731128044192759 0.85462688596819847 0
		 70.69616369179171 97.302822800904707 15.750357629348152 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_upperLeg_01_point" -p "C_hip_01_point";
	rename -uid "992F078F-4E53-3E06-35A5-1C861E37B882";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 2.2583 -5.5600995774539719 0.8344 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 90 -2.9616324232808893 -90 ;
	setAttr ".bps" -type "matrix" 0.10364511620844841 -0.99395841679336883 0.036115863159517259 0
		 0.10949094408245386 0.047492860074365817 0.99285253759351888 0 -0.98856938201123246 -0.09894995668304496 0.11375184843488628 0
		 8.6281999999999996 97.750199999999978 0.29140000000000055 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_lowerLeg_01_point" -p "L_upperLeg_01_point";
	rename -uid "C6985F57-4144-20B1-2483-2896226BC82E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 10.34000326013606 -2.2204460492503131e-16 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -9.5516761493650275 ;
	setAttr ".bps" -type "matrix" 0.091733361605610048 -0.99352520194792193 -0.06702733369958247 0
		 0.11964767995437353 -0.055826330407472917 0.99124560705950759 0 -0.98856938201123246 -0.09894995668304496 0.11375184843488628 0
		 13.280611611853208 53.133493982820909 1.9125652539180953 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_lowerLeg_02_endpoint" -p "L_lowerLeg_01_point";
	rename -uid "DE686552-41FC-9998-A7CD-4B8B5EFA8168";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" 10.916441577628497 2.2204460492503131e-16 -1.3322676295501878e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.091733361605610048 -0.99352520194792193 -0.06702733369958247 0
		 0.11964767995437353 -0.055826330407472917 0.99124560705950759 0 -0.98856938201123246 -0.09894995668304496 0.11375184843488628 0
		 17.150787097976934 11.217261827759259 -0.91527773846706939 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_foot_01_point" -p "L_lowerLeg_02_endpoint";
	rename -uid "8CA567DC-4038-D5CB-F396-7F93B25798FA";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" 0 0 8.8817841970012523e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 65.743152620707292 ;
	setAttr ".bps" -type "matrix" 0.10670166423050126 -0.46307425713110978 0.87987327907654533 0
		 0.055748287886651524 0.88631948663135607 0.45970631496123299 0 -0.9927269933109244 2.0967116931558394e-12 0.12038736126293156 0
		 17.150787097976934 11.217261827759259 -0.91527773846706895 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_foot_02_point" -p "L_foot_01_point";
	rename -uid "57E7936C-409B-D94B-7A8A-2AABA3DDB3ED";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" 6.2367963082529236 0 8.8817841970012523e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 5.8275385358309872 ;
	setAttr ".bps" -type "matrix" 0.11245964489945882 -0.35688515679545435 0.92735420046936312 0
		 0.042964462302456839 0.93414826706421905 0.3542895286626136 0 -0.9927269933109244 2.0967116931558394e-12 0.12038736126293156 0
		 18.918321506288031 3.5463441435310008 13.659999104091721 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "L_foot_03_endpoint" -p "L_foot_02_point";
	rename -uid "AB2BFA39-4206-A6C6-E3B3-E98E7E95A6E4";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" 2.7443797464533204 4.4408920985006262e-16 -8.8817841970012523e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0.11245964489945882 -0.35688515679545435 0.92735420046936312 0
		 0.042964462302456839 0.93414826706421905 0.3542895286626136 0 -0.9927269933109244 2.0967116931558394e-12 0.12038736126293156 0
		 19.991175272664378 0.14169543621804426 22.506865441149397 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_upperLeg_01_point" -p "C_hip_01_point";
	rename -uid "048E93D0-4EC2-E804-82C3-09AA784E86D7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" -2.2582 -5.5600995774539719 0.8344 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -90 2.9616324232808893 90 ;
	setAttr ".bps" -type "matrix" 0.10364511620844841 -0.99395841679336883 0.036115863159517259 0
		 0.10949094408245386 0.047492860074365817 0.99285253759351888 0 -0.98856938201123246 -0.09894995668304496 0.11375184843488628 0
		 8.6281999999999996 97.750199999999978 0.29140000000000055 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_lowerLeg_01_point" -p "R_upperLeg_01_point";
	rename -uid "A83036D1-42A5-15FE-0AC3-7E9B1F074CE2";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" -10.34 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.2074182704702916e-06 -8.9117810438511744e-15 -9.5516761493650186 ;
	setAttr ".bps" -type "matrix" 0.091733361605610048 -0.99352520194792193 -0.06702733369958247 0
		 0.11964767995437353 -0.055826330407472917 0.99124560705950759 0 -0.98856938201123246 -0.09894995668304496 0.11375184843488628 0
		 13.280611611853208 53.133493982820909 1.9125652539180953 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_lowerLeg_02_endpoint" -p "R_lowerLeg_01_point";
	rename -uid "78EC284C-4690-A874-626E-59B121698426";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".t" -type "double3" -10.915999999999997 4.4408920985006262e-16 -8.8817841970012523e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -1.2074182697257331e-06 -5.0268885606409513e-23 -1.8780174078092804e-22 ;
	setAttr ".bps" -type "matrix" 0.091733361605610048 -0.99352520194792193 -0.06702733369958247 0
		 0.11964767995437353 -0.055826330407472917 0.99124560705950759 0 -0.98856938201123246 -0.09894995668304496 0.11375184843488628 0
		 17.150787097976934 11.217261827759259 -0.91527773846706939 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_foot_01_point" -p "R_lowerLeg_02_endpoint";
	rename -uid "7E8A9A5D-45E7-04BE-AE8B-FAB2455AE820";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".t" -type "double3" -1.7763568394002505e-15 -4.4408920985006262e-16 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 1.7210386994797821e-06 1.895758319773386e-22 65.742679890990146 ;
	setAttr ".bps" -type "matrix" 0.10670166423050126 -0.46307425713110978 0.87987327907654533 0
		 0.055748287886651524 0.88631948663135607 0.45970631496123299 0 -0.9927269933109244 2.0967116931558394e-12 0.12038736126293156 0
		 17.150787097976934 11.217261827759259 -0.91527773846706895 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_foot_02_point" -p "R_foot_01_point";
	rename -uid "D9773837-42E1-5E6C-ECFA-5DAEAD4F4D86";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 5;
	setAttr ".t" -type "double3" -6.2370000000000019 3.1086244689504383e-15 2.9464868323003657e-08 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 2.5016560531166515e-06 0 5.8273306501314517 ;
	setAttr ".bps" -type "matrix" 0.11245964489945882 -0.35688515679545435 0.92735420046936312 0
		 0.042964462302456839 0.93414826706421905 0.3542895286626136 0 -0.9927269933109244 2.0967116931558394e-12 0.12038736126293156 0
		 18.918321506288031 3.5463441435310008 13.659999104091721 1;
	setAttr ".radi" 0.26999999999999991;
createNode joint -n "R_foot_03_endpoint" -p "R_foot_02_point";
	rename -uid "145D3725-4FA8-D07B-7028-ABAB04A8B2F8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 6;
	setAttr ".t" -type "double3" -2.7439999999999989 -2.6645352591003757e-15 -6.0003335633496135e-09 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 4.9045561968554791e-06 -3.5039391977565109e-21 -8.9882839998642463e-14 ;
	setAttr ".bps" -type "matrix" 0.11245964489945882 -0.35688515679545435 0.92735420046936312 0
		 0.042964462302456839 0.93414826706421905 0.3542895286626136 0 -0.9927269933109244 2.0967116931558394e-12 0.12038736126293156 0
		 19.991175272664378 0.14169543621804426 22.506865441149397 1;
	setAttr ".radi" 0.26999999999999991;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "F2F845C3-498F-90BB-95C2-128B639D99C9";
	setAttr -s 74 ".lnk";
	setAttr -s 73 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "23239322-45F2-94F0-32BE-0C8DF00D93F3";
	setAttr -s 8 ".bsdt";
	setAttr ".bsdt[0].bscd" -type "Int32Array" 3 -1 -2 -5 ;
	setAttr ".bsdt[1].bscd" -type "Int32Array" 0 ;
	setAttr ".bsdt[1].bsdn" -type "string" "pasted_";
	setAttr ".bsdt[2].bscd" -type "Int32Array" 1 -3 ;
	setAttr ".bsdt[2].bsdn" -type "string" "RIG_DuendeGino_setup_0007";
	setAttr ".bsdt[3].bscd" -type "Int32Array" 1 -4 ;
	setAttr ".bsdt[3].bspi" 2;
	setAttr ".bsdt[3].bsdn" -type "string" "jen_bipedTemplate";
	setAttr ".bsdt[4].bscd" -type "Int32Array" 0 ;
	setAttr ".bsdt[4].bspi" 3;
	setAttr ".bsdt[4].bsdn" -type "string" "pasted_";
	setAttr ".bsdt[5].bscd" -type "Int32Array" 1 -6 ;
	setAttr ".bsdt[5].bsdn" -type "string" "RIG_DuendeGino_setup_0008";
	setAttr ".bsdt[6].bscd" -type "Int32Array" 1 -7 ;
	setAttr ".bsdt[6].bspi" 5;
	setAttr ".bsdt[6].bsdn" -type "string" "jen_bipedTemplate";
	setAttr ".bsdt[7].bscd" -type "Int32Array" 0 ;
	setAttr ".bsdt[7].bspi" 6;
	setAttr ".bsdt[7].bsdn" -type "string" "pasted_";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "9D4EE6A9-4953-1B25-FF61-52B7442F1986";
createNode displayLayerManager -n "layerManager";
	rename -uid "465377B9-41E1-15C8-3263-5F9703368978";
	setAttr ".cdl" 5;
	setAttr -s 2 ".dli[1:2]"  4 5;
createNode displayLayer -n "defaultLayer";
	rename -uid "866A4D5D-4075-1448-4B9F-4B941A171CE8";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "432CADBA-429B-52EE-4353-7598CD4EA3C1";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "C2D89B73-4648-E341-ADB6-8EA6F899A5AC";
	setAttr ".g" yes;
createNode renderLayerManager -n "jen_bipedTemplate_renderLayerManager";
	rename -uid "4EC2B84C-480E-3BC4-DD8C-B59F58AC0642";
createNode renderLayer -n "jen_bipedTemplate_defaultRenderLayer";
	rename -uid "73AE3BC0-495B-492B-A1B3-8D9CA06424A0";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "7806024E-4234-4BCC-2D4E-CDB966EC2A0B";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"DCF_updateViewportList;updateModelPanelBar\" \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n"
		+ "            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n"
		+ "            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 606\n            -height 325\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n"
		+ "            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"DCF_updateViewportList;updateModelPanelBar\" \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n"
		+ "            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n"
		+ "            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n"
		+ "            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 605\n            -height 325\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"DCF_updateViewportList;updateModelPanelBar\" \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n"
		+ "            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n"
		+ "            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n"
		+ "            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 606\n            -height 325\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -docTag \"RADRENDER\" \n            -editorChanged \"DCF_updateViewportList;updateModelPanelBar\" \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n"
		+ "            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n"
		+ "            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1218\n            -height 694\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n"
		+ "            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n"
		+ "            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n"
		+ "            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n"
		+ "            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n"
		+ "            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n"
		+ "            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n"
		+ "                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n"
		+ "                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n                -showActiveCurveNames 0\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n"
		+ "                -valueLinesToggle 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n"
		+ "                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n"
		+ "                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n"
		+ "                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n"
		+ "                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n"
		+ "                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n"
		+ "                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n"
		+ "                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n"
		+ "                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\nstring $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"wireframe\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 1\n"
		+ "                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 32768\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n"
		+ "                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n"
		+ "                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n"
		+ "            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n"
		+ "            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -docTag \\\"RADRENDER\\\" \\n    -editorChanged \\\"DCF_updateViewportList;updateModelPanelBar\\\" \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1218\\n    -height 694\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -docTag \\\"RADRENDER\\\" \\n    -editorChanged \\\"DCF_updateViewportList;updateModelPanelBar\\\" \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1218\\n    -height 694\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 2 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "8BC179F7-44D6-BEAC-C8F2-97B5071D3A48";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode ilrOptionsNode -s -n "TurtleRenderOptions";
	rename -uid "6E4D9B89-4B0A-6194-AC20-1F90BAFA2940";
lockNode -l 1 ;
createNode ilrUIOptionsNode -s -n "TurtleUIOptions";
	rename -uid "FB0CCE86-41D1-01C6-A059-76B8FBBB2E93";
lockNode -l 1 ;
createNode ilrBakeLayerManager -s -n "TurtleBakeLayerManager";
	rename -uid "37115BFD-4E64-B858-4211-F6A6CCEFC7C7";
lockNode -l 1 ;
createNode ilrBakeLayer -s -n "TurtleDefaultBakeLayer";
	rename -uid "4B5EA2C6-450A-E3D6-9A5D-D1850A93A631";
lockNode -l 1 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "8CCB9196-443B-06EE-C37E-BAB7C672847F";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -96.831102695614462 -101.19047216952812 ;
	setAttr ".tgi[0].vh" -type "double2" 99.212054981956314 98.809519883186269 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo2";
	rename -uid "DFBF8C61-439F-8697-F296-F296303A7BC8";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo3";
	rename -uid "27D88B98-48AE-09D9-276C-639622445D55";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo4";
	rename -uid "54323193-450D-8D04-E847-62B09146BA40";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349701 -2196.54862394461 ;
	setAttr ".tgi[0].vh" -type "double2" 2157.1427714257052 2177.5010056538754 ;
createNode nodeGraphEditorInfo -n "MOD_MessiHero_PrePublish_hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "D56E07E2-446F-F2FF-BF2F-30803B880E00";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -323.80951094248991 -330.95236780151544 ;
	setAttr ".tgi[0].vh" -type "double2" 324.99998708566085 329.76189165834455 ;
createNode nodeGraphEditorInfo -n "MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "760779FF-475A-9EA3-48A4-6D834506C31F";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -316.07141601187891 -337.49998658895549 ;
	setAttr ".tgi[0].vh" -type "double2" 332.73808201627179 323.21427287090449 ;
createNode animCurveTL -n "animCurveTL1";
	rename -uid "94135D43-404D-D698-D0B7-FE9E15746AF6";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
createNode animCurveTU -n "animCurveTU1";
	rename -uid "C1BAD784-49FB-4548-5AFB-C28136C21E15";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo5";
	rename -uid "37BCAA6C-48C5-3B62-C248-A98FC4B3F28E";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6924.5418493855532 -7077.2890960631776 ;
	setAttr ".tgi[0].vh" -type "double2" 6949.9997238318247 7051.8312216169061 ;
createNode nodeGraphEditorInfo -n "MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "9D3968D1-4EFC-F58F-BF07-248CF6DCB049";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo6";
	rename -uid "1B3CEFC1-4183-FCF9-20CE-0E87C4FAD015";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "4915BA65-446A-8AF5-77B8-AE8C170D1295";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -96.831102695614462 -101.19047216952812 ;
	setAttr ".tgi[0].vh" -type "double2" 99.212054981956314 98.809519883186269 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo2";
	rename -uid "2B27B0BC-40A5-B48C-8442-6586560D4B01";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo3";
	rename -uid "C4DADFC7-4301-428F-FF25-14B2C6597E74";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo4";
	rename -uid "B648ED89-4B88-E961-38A1-A7A9A2F69598";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349701 -2196.54862394461 ;
	setAttr ".tgi[0].vh" -type "double2" 2157.1427714257052 2177.5010056538754 ;
createNode nodeGraphEditorInfo -n "pasted__MOD_MessiHero_PrePublish_hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "1EB2C481-416C-3A0C-2839-D9872A4ECEC7";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -323.80951094248991 -330.95236780151544 ;
	setAttr ".tgi[0].vh" -type "double2" 324.99998708566085 329.76189165834455 ;
createNode nodeGraphEditorInfo -n "pasted__MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "F0630D39-43E7-5A4F-4B29-AAB70DD5C319";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -316.07141601187891 -337.49998658895549 ;
	setAttr ".tgi[0].vh" -type "double2" 332.73808201627179 323.21427287090449 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo5";
	rename -uid "E1421F10-425B-4A9C-CC42-2CA38AB1ECAC";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6924.5418493855532 -7077.2890960631776 ;
	setAttr ".tgi[0].vh" -type "double2" 6949.9997238318247 7051.8312216169061 ;
createNode nodeGraphEditorInfo -n "pasted__MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "3CF01995-4C17-758F-E885-EFA5458A5410";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo6";
	rename -uid "8C0985C2-4BBF-E4E0-E16D-F5AF424EE374";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo";
	rename -uid "030660A3-47D9-CCAF-FAD4-738CE8D76B53";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -4280.7104766039447 -3213.09511041831 ;
	setAttr ".tgi[0].vh" -type "double2" 77.05950341883441 -1158.3332873053041 ;
createNode renderLayerManager -n "renderLayerManager1";
	rename -uid "B8A2F3A6-4BB7-FDDF-A753-6C8ED45CDC5D";
createNode renderLayer -n "defaultRenderLayer1";
	rename -uid "03F4C3B8-41EE-F70C-33AC-ADA84FBE954D";
	setAttr ".g" yes;
createNode renderLayerManager -n "jen_bipedTemplate_renderLayerManager2";
	rename -uid "03009742-4368-527D-4D55-A6B101BF1A45";
createNode renderLayer -n "jen_bipedTemplate_defaultRenderLayer1";
	rename -uid "FD48CBE9-4AB4-D6B5-1B37-0D895C54CD96";
	setAttr ".g" yes;
createNode renderLayerManager -n "jen_bipedTemplate_renderLayerManager1";
	rename -uid "D703C0C5-4381-6ABD-8790-2CBC7B1831C4";
createNode renderLayer -n "jen_bipedTemplate_jen_bipedTemplate_defaultRenderLayer";
	rename -uid "CA5D2236-4B5B-1C26-A1F0-6C83E283771C";
	setAttr ".g" yes;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo9";
	rename -uid "F313331E-421E-4BBF-51E4-69832E014F2B";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -96.831102695614462 -101.19047216952812 ;
	setAttr ".tgi[0].vh" -type "double2" 99.212054981956314 98.809519883186269 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo10";
	rename -uid "349FF8A5-4A8E-EE31-5847-318D5E834968";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo11";
	rename -uid "665EE530-403F-4626-239A-9EB4AB565F10";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo12";
	rename -uid "005C3CA9-4CFC-6DA6-AD18-AE89E30F711D";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349701 -2196.54862394461 ;
	setAttr ".tgi[0].vh" -type "double2" 2157.1427714257052 2177.5010056538754 ;
createNode nodeGraphEditorInfo -n "MOD_MessiHero_PrePublish_hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "94220293-47D4-49D4-EED7-C79D82DADE9A";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -323.80951094248991 -330.95236780151544 ;
	setAttr ".tgi[0].vh" -type "double2" 324.99998708566085 329.76189165834455 ;
createNode nodeGraphEditorInfo -n "MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo2";
	rename -uid "99099663-410E-1EBA-770E-40AFF7816D8B";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -316.07141601187891 -337.49998658895549 ;
	setAttr ".tgi[0].vh" -type "double2" 332.73808201627179 323.21427287090449 ;
createNode animCurveTL -n "animCurveTL2";
	rename -uid "8D0A001E-49BC-6A87-C0AC-82BB8CB78630";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
createNode animCurveTU -n "animCurveTU2";
	rename -uid "E5B034D8-49E6-DAAF-6D5B-A4853A19DB0C";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo13";
	rename -uid "3CD1AC7D-48FE-8D1C-4F1F-729892E77507";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6924.5418493855532 -7077.2890960631776 ;
	setAttr ".tgi[0].vh" -type "double2" 6949.9997238318247 7051.8312216169061 ;
createNode nodeGraphEditorInfo -n "MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo3";
	rename -uid "54B1CAC0-4A24-A1FC-E6ED-13B49E0958EF";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo14";
	rename -uid "5357AB13-431A-64C8-2F7A-C3A6E43014D1";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo7";
	rename -uid "405C4045-4C18-70E9-BAEB-AD903C7ED4BF";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -96.831102695614462 -101.19047216952812 ;
	setAttr ".tgi[0].vh" -type "double2" 99.212054981956314 98.809519883186269 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo8";
	rename -uid "209341FC-4C6F-6576-5FEA-D4964CFB96C6";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo9";
	rename -uid "12EE0F57-45A0-CED6-6515-E2ADB6A994F4";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo10";
	rename -uid "82793692-4F42-A370-A01F-099AC9DDA4B4";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349701 -2196.54862394461 ;
	setAttr ".tgi[0].vh" -type "double2" 2157.1427714257052 2177.5010056538754 ;
createNode nodeGraphEditorInfo -n "pasted__MOD_MessiHero_PrePublish_hyperShadePrimaryNodeEditorSavedTabsInfo1";
	rename -uid "8BEBE981-4253-ACFE-5439-27A0195E9615";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -323.80951094248991 -330.95236780151544 ;
	setAttr ".tgi[0].vh" -type "double2" 324.99998708566085 329.76189165834455 ;
createNode nodeGraphEditorInfo -n "pasted__MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo2";
	rename -uid "2BE2E00D-4DE8-E70A-6D72-9DA2600A2F6D";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -316.07141601187891 -337.49998658895549 ;
	setAttr ".tgi[0].vh" -type "double2" 332.73808201627179 323.21427287090449 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo11";
	rename -uid "48337BC9-4FE9-1E0C-261C-418D4E6BF27A";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6924.5418493855532 -7077.2890960631776 ;
	setAttr ".tgi[0].vh" -type "double2" 6949.9997238318247 7051.8312216169061 ;
createNode nodeGraphEditorInfo -n "pasted__MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo3";
	rename -uid "B2F76CC5-4887-68DA-ADF4-D3988C1C0AC2";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo12";
	rename -uid "41FE2B66-442A-94FD-BBDD-6DAFF0FC7495";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo8";
	rename -uid "BE6D17B8-4D50-1855-211B-B3AF8E4063B7";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -4280.7104766039447 -3213.09511041831 ;
	setAttr ".tgi[0].vh" -type "double2" 77.05950341883441 -1158.3332873053041 ;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo1";
	rename -uid "965C26FD-4B7C-6DC4-3991-D2A5D2D6CECA";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -853.57139465354885 -479.76188569788036 ;
	setAttr ".tgi[0].vh" -type "double2" 854.76187079671979 478.57140955470936 ;
createNode renderLayerManager -n "renderLayerManager4";
	rename -uid "E1223BB9-4863-DAFD-4581-16BC26B83953";
createNode renderLayer -n "defaultRenderLayer4";
	rename -uid "4B8B4AE0-47CE-7255-9607-439E78619118";
	setAttr ".g" yes;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo23";
	rename -uid "040EA480-40C1-4A37-B799-B1A6264F316F";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -5607.406058843304 -2708.0140767903522 ;
	setAttr ".tgi[0].vh" -type "double2" 3494.0829411981449 2744.9188372286503 ;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo2";
	rename -uid "46F253F8-4447-7BC6-54B7-F3BC9F1A47AF";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" 34.57469638087462 -273.86348529331519 ;
	setAttr ".tgi[0].vh" -type "double2" 860.16990166990684 418.0537398647208 ;
	setAttr -s 15 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -98.571426391601563;
	setAttr ".tgi[0].ni[0].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" 191.42857360839844;
	setAttr ".tgi[0].ni[1].y" -182.85714721679688;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" 515.71429443359375;
	setAttr ".tgi[0].ni[2].y" 251.42857360839844;
	setAttr ".tgi[0].ni[2].nvs" 18304;
	setAttr ".tgi[0].ni[3].x" 205.71427917480469;
	setAttr ".tgi[0].ni[3].y" -197.14285278320313;
	setAttr ".tgi[0].ni[3].nvs" 18304;
	setAttr ".tgi[0].ni[4].x" 512.85711669921875;
	setAttr ".tgi[0].ni[4].y" -197.14285278320313;
	setAttr ".tgi[0].ni[4].nvs" 18304;
	setAttr ".tgi[0].ni[5].x" -405.71429443359375;
	setAttr ".tgi[0].ni[5].y" 178.57142639160156;
	setAttr ".tgi[0].ni[5].nvs" 18304;
	setAttr ".tgi[0].ni[6].x" -98.571426391601563;
	setAttr ".tgi[0].ni[6].y" 230;
	setAttr ".tgi[0].ni[6].nvs" 18304;
	setAttr ".tgi[0].ni[7].x" -405.71429443359375;
	setAttr ".tgi[0].ni[7].y" -52.857143402099609;
	setAttr ".tgi[0].ni[7].nvs" 18304;
	setAttr ".tgi[0].ni[8].x" -712.85711669921875;
	setAttr ".tgi[0].ni[8].y" 230;
	setAttr ".tgi[0].ni[8].nvs" 18304;
	setAttr ".tgi[0].ni[9].x" -405.71429443359375;
	setAttr ".tgi[0].ni[9].y" 280;
	setAttr ".tgi[0].ni[9].nvs" 18304;
	setAttr ".tgi[0].ni[10].x" 208.57142639160156;
	setAttr ".tgi[0].ni[10].y" 230;
	setAttr ".tgi[0].ni[10].nvs" 18304;
	setAttr ".tgi[0].ni[11].x" 515.71429443359375;
	setAttr ".tgi[0].ni[11].y" 20;
	setAttr ".tgi[0].ni[11].nvs" 18304;
	setAttr ".tgi[0].ni[12].x" 208.57142639160156;
	setAttr ".tgi[0].ni[12].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[12].nvs" 18304;
	setAttr ".tgi[0].ni[13].x" -405.71429443359375;
	setAttr ".tgi[0].ni[13].y" 48.571430206298828;
	setAttr ".tgi[0].ni[13].nvs" 18304;
	setAttr ".tgi[0].ni[14].x" -712.85711669921875;
	setAttr ".tgi[0].ni[14].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[14].nvs" 18304;
createNode renderLayerManager -n "renderLayerManager3";
	rename -uid "ABFCB42C-40EF-1B2B-804E-21AE943CBB12";
createNode renderLayer -n "defaultRenderLayer3";
	rename -uid "44D267A6-4A02-35F0-4E55-C9B376840ED4";
	setAttr ".g" yes;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo22";
	rename -uid "BDA75629-41F7-10E9-5AD7-7D9066188D08";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -5607.406058843304 -2708.0140767903522 ;
	setAttr ".tgi[0].vh" -type "double2" 3494.0829411981449 2744.9188372286503 ;
createNode renderLayerManager -n "renderLayerManager2";
	rename -uid "002ACFD3-4BA4-FABC-95F0-1BAC9ECB3420";
createNode renderLayer -n "defaultRenderLayer2";
	rename -uid "96CE3B9A-4D47-50C9-9844-A5835D610723";
	setAttr ".g" yes;
createNode renderLayerManager -n "jen_bipedTemplate_renderLayerManager4";
	rename -uid "B8489A3B-43F0-5C65-F8C6-E8960AB461E8";
createNode renderLayer -n "jen_bipedTemplate_defaultRenderLayer2";
	rename -uid "03CA23E6-41FA-8A63-CE20-948CE2C3470B";
	setAttr ".g" yes;
createNode renderLayerManager -n "jen_bipedTemplate_renderLayerManager3";
	rename -uid "3A0FA629-4850-C20D-4902-239898091A48";
createNode renderLayer -n "jen_bipedTemplate_jen_bipedTemplate_defaultRenderLayer1";
	rename -uid "D76B4987-4736-AB55-ADCB-A18F20F14622";
	setAttr ".g" yes;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo16";
	rename -uid "1D1FDC6C-4238-DF99-387E-B78A8679E344";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -96.831102695614462 -101.19047216952812 ;
	setAttr ".tgi[0].vh" -type "double2" 99.212054981956314 98.809519883186269 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo17";
	rename -uid "76C94179-4DD6-17F2-E683-F89965AE4427";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo18";
	rename -uid "6333B1E3-41F9-557E-20DE-888FA314C58B";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo19";
	rename -uid "8D9C908D-48D1-3D80-872C-2FA32CF23D5B";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349701 -2196.54862394461 ;
	setAttr ".tgi[0].vh" -type "double2" 2157.1427714257052 2177.5010056538754 ;
createNode nodeGraphEditorInfo -n "MOD_MessiHero_PrePublish_hyperShadePrimaryNodeEditorSavedTabsInfo2";
	rename -uid "76AD4FF5-40C3-5E1C-73ED-05A5FBE3485E";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -323.80951094248991 -330.95236780151544 ;
	setAttr ".tgi[0].vh" -type "double2" 324.99998708566085 329.76189165834455 ;
createNode nodeGraphEditorInfo -n "MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo4";
	rename -uid "8BB1F795-40CF-DD4F-281C-B597C8C76342";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -316.07141601187891 -337.49998658895549 ;
	setAttr ".tgi[0].vh" -type "double2" 332.73808201627179 323.21427287090449 ;
createNode animCurveTL -n "animCurveTL3";
	rename -uid "A7E4FC72-4424-10E8-9D1E-66A2416B8DF8";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
createNode animCurveTU -n "animCurveTU3";
	rename -uid "8D1E91D9-48B7-BDE8-C27C-AF95EB6AF5C3";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo20";
	rename -uid "5F1568A7-436B-7A1B-2571-A1BD05902603";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6924.5418493855532 -7077.2890960631776 ;
	setAttr ".tgi[0].vh" -type "double2" 6949.9997238318247 7051.8312216169061 ;
createNode nodeGraphEditorInfo -n "MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo5";
	rename -uid "A91AC6C5-4B2F-E598-9538-70ADB5F29F1C";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo21";
	rename -uid "C50C8E26-46C9-3854-1A03-53B998CEC212";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo13";
	rename -uid "B37D6169-4FDA-4C58-07F3-419CA8D542B6";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -96.831102695614462 -101.19047216952812 ;
	setAttr ".tgi[0].vh" -type "double2" 99.212054981956314 98.809519883186269 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo14";
	rename -uid "BB958557-451C-8F7C-AE97-118E5E5E8910";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo15";
	rename -uid "BC08B2CD-4544-ED70-3C13-E9AB2B3E1489";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349706 -2194.145828059311 ;
	setAttr ".tgi[0].vh" -type "double2" 2154.7618191393631 2177.4791620549181 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo16";
	rename -uid "0F324D26-4652-2628-194E-AD8CCC044BA3";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2138.0951531349701 -2196.54862394461 ;
	setAttr ".tgi[0].vh" -type "double2" 2157.1427714257052 2177.5010056538754 ;
createNode nodeGraphEditorInfo -n "pasted__MOD_MessiHero_PrePublish_hyperShadePrimaryNodeEditorSavedTabsInfo2";
	rename -uid "AFFC19A5-4EFE-FE43-2213-A8A29069F6F3";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -323.80951094248991 -330.95236780151544 ;
	setAttr ".tgi[0].vh" -type "double2" 324.99998708566085 329.76189165834455 ;
createNode nodeGraphEditorInfo -n "pasted__MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo4";
	rename -uid "307F82D1-4451-DD28-6963-96B47E37DF54";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -316.07141601187891 -337.49998658895549 ;
	setAttr ".tgi[0].vh" -type "double2" 332.73808201627179 323.21427287090449 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo17";
	rename -uid "9073B448-4A6E-D777-CC15-4CBF3511F395";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6924.5418493855532 -7077.2890960631776 ;
	setAttr ".tgi[0].vh" -type "double2" 6949.9997238318247 7051.8312216169061 ;
createNode nodeGraphEditorInfo -n "pasted__MOD_MessiHero_hyperShadePrimaryNodeEditorSavedTabsInfo5";
	rename -uid "0810C0DB-44F5-BC7F-68BF-F99105D76AE9";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "pasted__hyperShadePrimaryNodeEditorSavedTabsInfo18";
	rename -uid "DFC0BB8D-40A9-57C3-70CF-B09093549BEE";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -6985.7140081269563 -8849.0057645800553 ;
	setAttr ".tgi[0].vh" -type "double2" 9904.7615111820414 8351.386736734612 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo15";
	rename -uid "913FAE91-49F3-F7FE-5437-14BC9D75CC12";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -4280.7104766039447 -3213.09511041831 ;
	setAttr ".tgi[0].vh" -type "double2" 77.05950341883441 -1158.3332873053041 ;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo3";
	rename -uid "75379B9E-43CA-3B10-28B2-8A89BA0A90A6";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -853.57139465354885 -479.76188569788036 ;
	setAttr ".tgi[0].vh" -type "double2" 854.76187079671979 478.57140955470936 ;
createNode renderLayerManager -n "renderLayerManager6";
	rename -uid "CB0B560C-4789-7AA0-A163-2697800832E5";
createNode renderLayer -n "defaultRenderLayer6";
	rename -uid "3CDAA183-4FDE-80A1-534F-E38699BAD405";
	setAttr ".g" yes;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo28";
	rename -uid "9FBCC86E-4E6D-22E6-6D47-9FAF7BFB0FB2";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -5607.406058843304 -2708.0140767903522 ;
	setAttr ".tgi[0].vh" -type "double2" 3494.0829411981449 2744.9188372286503 ;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo4";
	rename -uid "065AE737-46A5-AF22-3CE1-B18F0828A560";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" 34.57469638087462 -273.86348529331519 ;
	setAttr ".tgi[0].vh" -type "double2" 860.16990166990684 418.0537398647208 ;
	setAttr -s 15 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -98.571426391601563;
	setAttr ".tgi[0].ni[0].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" 191.42857360839844;
	setAttr ".tgi[0].ni[1].y" -182.85714721679688;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" 515.71429443359375;
	setAttr ".tgi[0].ni[2].y" 251.42857360839844;
	setAttr ".tgi[0].ni[2].nvs" 18304;
	setAttr ".tgi[0].ni[3].x" 205.71427917480469;
	setAttr ".tgi[0].ni[3].y" -197.14285278320313;
	setAttr ".tgi[0].ni[3].nvs" 18304;
	setAttr ".tgi[0].ni[4].x" 512.85711669921875;
	setAttr ".tgi[0].ni[4].y" -197.14285278320313;
	setAttr ".tgi[0].ni[4].nvs" 18304;
	setAttr ".tgi[0].ni[5].x" -405.71429443359375;
	setAttr ".tgi[0].ni[5].y" 178.57142639160156;
	setAttr ".tgi[0].ni[5].nvs" 18304;
	setAttr ".tgi[0].ni[6].x" -98.571426391601563;
	setAttr ".tgi[0].ni[6].y" 230;
	setAttr ".tgi[0].ni[6].nvs" 18304;
	setAttr ".tgi[0].ni[7].x" -405.71429443359375;
	setAttr ".tgi[0].ni[7].y" -52.857143402099609;
	setAttr ".tgi[0].ni[7].nvs" 18304;
	setAttr ".tgi[0].ni[8].x" -712.85711669921875;
	setAttr ".tgi[0].ni[8].y" 230;
	setAttr ".tgi[0].ni[8].nvs" 18304;
	setAttr ".tgi[0].ni[9].x" -405.71429443359375;
	setAttr ".tgi[0].ni[9].y" 280;
	setAttr ".tgi[0].ni[9].nvs" 18304;
	setAttr ".tgi[0].ni[10].x" 208.57142639160156;
	setAttr ".tgi[0].ni[10].y" 230;
	setAttr ".tgi[0].ni[10].nvs" 18304;
	setAttr ".tgi[0].ni[11].x" 515.71429443359375;
	setAttr ".tgi[0].ni[11].y" 20;
	setAttr ".tgi[0].ni[11].nvs" 18304;
	setAttr ".tgi[0].ni[12].x" 208.57142639160156;
	setAttr ".tgi[0].ni[12].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[12].nvs" 18304;
	setAttr ".tgi[0].ni[13].x" -405.71429443359375;
	setAttr ".tgi[0].ni[13].y" 48.571430206298828;
	setAttr ".tgi[0].ni[13].nvs" 18304;
	setAttr ".tgi[0].ni[14].x" -712.85711669921875;
	setAttr ".tgi[0].ni[14].y" -1.4285714626312256;
	setAttr ".tgi[0].ni[14].nvs" 18304;
createNode renderLayerManager -n "renderLayerManager5";
	rename -uid "1EDB142F-4E2C-7BF9-E7BC-CFAD08AB0165";
createNode renderLayer -n "defaultRenderLayer5";
	rename -uid "148F0092-4403-C708-568B-61BAC831769D";
	setAttr ".g" yes;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo25";
	rename -uid "25EA9177-4C41-D5C2-1052-52B2F253A460";
	setAttr ".def" no;
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -5607.406058843304 -2708.0140767903522 ;
	setAttr ".tgi[0].vh" -type "double2" 3494.0829411981449 2744.9188372286503 ;
createNode nodeGraphEditorInfo -n "hyperShadePrimaryNodeEditorSavedTabsInfo29";
	rename -uid "485FB80E-4304-22F4-890C-5FBD855C8329";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -1666.4306895705481 -732.84509975659137 ;
	setAttr ".tgi[0].vh" -type "double2" 1592.7697051668608 745.94033733147126 ;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "2687C94C-4272-3627-E416-E99D7A88B1C0";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2342.388261227306 -2184.8105472816278 ;
	setAttr ".tgi[0].vh" -type "double2" 2381.4210748748997 2202.4579682433482 ;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr -av -k on ".unw" 1;
	setAttr -av -k on ".etw";
	setAttr -av -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr -av -k on ".ihi";
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr -av ".ta";
	setAttr -av ".tq";
	setAttr -av ".aoam";
	setAttr -av ".aora";
	setAttr -av ".hfe";
	setAttr -av ".mbe";
	setAttr -av -k on ".mbsof";
select -ne :renderPartition;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
	setAttr -s 12 ".r";
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w";
	setAttr -av -k on ".h";
	setAttr -av -k on ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar";
	setAttr -av -k on ".ldar";
	setAttr -av -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -av -k on ".isu";
	setAttr -av -k on ".pdu";
select -ne :defaultColorMgtGlobals;
	setAttr ".cme" no;
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k off -cb on ".ctrs" 256;
	setAttr -av -k off -cb on ".btrs" 512;
	setAttr -k off -cb on ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off -cb on ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
connectAttr "C_hip_01_point.s" "C_spine_01_point.is";
connectAttr "C_spine_01_point.s" "C_spine_02_point.is";
connectAttr "C_spine_02_point.s" "C_spine_03_point.is";
connectAttr "C_spine_03_point.s" "C_spine_04_point.is";
connectAttr "C_spine_04_point.s" "C_spine_05_point.is";
connectAttr "C_spine_05_point.s" "C_spine_06_point.is";
connectAttr "C_spine_06_point.s" "C_spine_07_point.is";
connectAttr "C_spine_07_point.s" "C_spine_08_endpoint.is";
connectAttr "C_spine_08_endpoint.s" "C_chest_01_point.is";
connectAttr "C_chest_01_point.s" "C_chest_01_endpoint.is";
connectAttr "C_chest_01_endpoint.s" "C_neck_01_point.is";
connectAttr "C_neck_01_point.s" "C_neck_01_endpoint.is";
connectAttr "C_neck_01_endpoint.s" "C_head_01_point.is";
connectAttr "C_head_01_point.s" "C_head_02_endpoint.is";
connectAttr "C_chest_01_point.s" "L_clavicle_01_point.is";
connectAttr "L_clavicle_01_point.s" "L_upperArm_01_point.is";
connectAttr "L_upperArm_01_point.s" "L_lowerArm_01_point.is";
connectAttr "L_lowerArm_01_point.s" "L_lowerArm_02_endpoint.is";
connectAttr "L_hand_01_point.s" "L_fingerThumb_01_point.is";
connectAttr "L_fingerThumb_01_point.s" "L_fingerThumb_02_point.is";
connectAttr "L_fingerThumb_02_point.s" "L_fingerThumb_03_point.is";
connectAttr "L_fingerThumb_03_point.s" "L_fingerThumb_04_endpoint.is";
connectAttr "L_hand_01_point.s" "L_fingerRing_01_point.is";
connectAttr "L_fingerRing_01_point.s" "L_fingerRing_02_point.is";
connectAttr "L_fingerRing_02_point.s" "L_fingerRing_03_point.is";
connectAttr "L_fingerRing_03_point.s" "L_fingerRing_04_point.is";
connectAttr "L_fingerRing_04_point.s" "L_fingerRing_05_endpoint.is";
connectAttr "L_hand_01_point.s" "L_fingerPinky_01_point.is";
connectAttr "L_fingerPinky_01_point.s" "L_fingerPinky_02_point.is";
connectAttr "L_fingerPinky_02_point.s" "L_fingerPinky_03_point.is";
connectAttr "L_fingerPinky_03_point.s" "L_fingerPinky_04_point.is";
connectAttr "L_fingerPinky_04_point.s" "L_fingerPinky_05_endpoint.is";
connectAttr "L_hand_01_point.s" "L_handEnd_01_endpoint.is";
connectAttr "L_hand_01_point.s" "L_fingerMiddle_01_point.is";
connectAttr "L_fingerMiddle_01_point.s" "L_fingerMiddle_02_point.is";
connectAttr "L_fingerMiddle_02_point.s" "L_fingerMiddle_03_point.is";
connectAttr "L_fingerMiddle_03_point.s" "L_fingerMiddle_04_point.is";
connectAttr "L_fingerMiddle_04_point.s" "L_fingerMiddle_05_endpoint.is";
connectAttr "L_hand_01_point.s" "L_fingerIndex_01_point.is";
connectAttr "L_fingerIndex_01_point.s" "L_fingerIndex_02_point.is";
connectAttr "L_fingerIndex_02_point.s" "L_fingerIndex_03_point.is";
connectAttr "L_fingerIndex_03_point.s" "L_fingerIndex_04_point.is";
connectAttr "L_fingerIndex_04_point.s" "L_fingerIndex_05_endpoint.is";
connectAttr "C_chest_01_point.s" "R_clavicle_01_point.is";
connectAttr "R_clavicle_01_point.s" "R_upperArm_01_point.is";
connectAttr "R_upperArm_01_point.s" "R_lowerArm_01_point.is";
connectAttr "R_lowerArm_01_point.s" "R_lowerArm_02_endpoint.is";
connectAttr "R_hand_01_point.s" "R_fingerThumb_01_point.is";
connectAttr "R_fingerThumb_01_point.s" "R_fingerThumb_02_point.is";
connectAttr "R_fingerThumb_02_point.s" "R_fingerThumb_03_point.is";
connectAttr "R_fingerThumb_03_point.s" "R_fingerThumb_04_endpoint.is";
connectAttr "R_hand_01_point.s" "R_fingerRing_01_point.is";
connectAttr "R_fingerRing_01_point.s" "R_fingerRing_02_point.is";
connectAttr "R_fingerRing_02_point.s" "R_fingerRing_03_point.is";
connectAttr "R_fingerRing_03_point.s" "R_fingerRing_04_point.is";
connectAttr "R_fingerRing_04_point.s" "R_fingerRing_05_endpoint.is";
connectAttr "R_hand_01_point.s" "R_fingerPinky_01_point.is";
connectAttr "R_fingerPinky_01_point.s" "R_fingerPinky_02_point.is";
connectAttr "R_fingerPinky_02_point.s" "R_fingerPinky_03_point.is";
connectAttr "R_fingerPinky_03_point.s" "R_fingerPinky_04_point.is";
connectAttr "R_fingerPinky_04_point.s" "R_fingerPinky_05_endpoint.is";
connectAttr "R_hand_01_point.s" "R_handEnd_01_endpoint.is";
connectAttr "R_hand_01_point.s" "R_fingerMiddle_01_point.is";
connectAttr "R_fingerMiddle_01_point.s" "R_fingerMiddle_02_point.is";
connectAttr "R_fingerMiddle_02_point.s" "R_fingerMiddle_03_point.is";
connectAttr "R_fingerMiddle_03_point.s" "R_fingerMiddle_04_point.is";
connectAttr "R_fingerMiddle_04_point.s" "R_fingerMiddle_05_endpoint.is";
connectAttr "R_hand_01_point.s" "R_fingerIndex_01_point.is";
connectAttr "R_fingerIndex_01_point.s" "R_fingerIndex_02_point.is";
connectAttr "R_fingerIndex_02_point.s" "R_fingerIndex_03_point.is";
connectAttr "R_fingerIndex_03_point.s" "R_fingerIndex_04_point.is";
connectAttr "R_fingerIndex_04_point.s" "R_fingerIndex_05_endpoint.is";
connectAttr "C_hip_01_point.s" "L_upperLeg_01_point.is";
connectAttr "L_upperLeg_01_point.s" "L_lowerLeg_01_point.is";
connectAttr "L_lowerLeg_01_point.s" "L_lowerLeg_02_endpoint.is";
connectAttr "L_foot_02_point.s" "L_foot_03_endpoint.is";
connectAttr "C_hip_01_point.s" "R_upperLeg_01_point.is";
connectAttr "R_upperLeg_01_point.s" "R_lowerLeg_01_point.is";
connectAttr "R_lowerLeg_01_point.s" "R_lowerLeg_02_endpoint.is";
connectAttr "R_foot_02_point.s" "R_foot_03_endpoint.is";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":ikSystem.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":defaultHardwareRenderGlobals.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":defaultHardwareRenderGlobals.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "jen_bipedTemplate_renderLayerManager.rlmi[0]" "jen_bipedTemplate_defaultRenderLayer.rlid"
		;
connectAttr ":TurtleDefaultBakeLayer.idx" ":TurtleBakeLayerManager.bli[0]";
connectAttr ":TurtleRenderOptions.msg" ":TurtleDefaultBakeLayer.rset";
connectAttr "renderLayerManager1.rlmi[0]" "defaultRenderLayer1.rlid";
connectAttr "jen_bipedTemplate_renderLayerManager2.rlmi[0]" "jen_bipedTemplate_defaultRenderLayer1.rlid"
		;
connectAttr "jen_bipedTemplate_renderLayerManager1.rlmi[0]" "jen_bipedTemplate_jen_bipedTemplate_defaultRenderLayer.rlid"
		;
connectAttr "renderLayerManager4.rlmi[0]" "defaultRenderLayer4.rlid";
connectAttr ":initialShadingGroup.msg" "MayaNodeEditorSavedTabsInfo2.tgi[0].ni[3].dn"
		;
connectAttr "renderLayerManager3.rlmi[0]" "defaultRenderLayer3.rlid";
connectAttr "renderLayerManager2.rlmi[0]" "defaultRenderLayer2.rlid";
connectAttr "jen_bipedTemplate_renderLayerManager4.rlmi[0]" "jen_bipedTemplate_defaultRenderLayer2.rlid"
		;
connectAttr "jen_bipedTemplate_renderLayerManager3.rlmi[0]" "jen_bipedTemplate_jen_bipedTemplate_defaultRenderLayer1.rlid"
		;
connectAttr "renderLayerManager6.rlmi[0]" "defaultRenderLayer6.rlid";
connectAttr ":initialShadingGroup.msg" "MayaNodeEditorSavedTabsInfo4.tgi[0].ni[3].dn"
		;
connectAttr "renderLayerManager5.rlmi[0]" "defaultRenderLayer5.rlid";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "jen_bipedTemplate_defaultRenderLayer.msg" ":defaultRenderingList1.r"
		 -na;
connectAttr "defaultRenderLayer1.msg" ":defaultRenderingList1.r" -na;
connectAttr "jen_bipedTemplate_defaultRenderLayer1.msg" ":defaultRenderingList1.r"
		 -na;
connectAttr "jen_bipedTemplate_jen_bipedTemplate_defaultRenderLayer.msg" ":defaultRenderingList1.r"
		 -na;
connectAttr "defaultRenderLayer4.msg" ":defaultRenderingList1.r" -na;
connectAttr "defaultRenderLayer3.msg" ":defaultRenderingList1.r" -na;
connectAttr "defaultRenderLayer2.msg" ":defaultRenderingList1.r" -na;
connectAttr "jen_bipedTemplate_defaultRenderLayer2.msg" ":defaultRenderingList1.r"
		 -na;
connectAttr "jen_bipedTemplate_jen_bipedTemplate_defaultRenderLayer1.msg" ":defaultRenderingList1.r"
		 -na;
connectAttr "defaultRenderLayer6.msg" ":defaultRenderingList1.r" -na;
connectAttr "defaultRenderLayer5.msg" ":defaultRenderingList1.r" -na;
// End of jen_bipedTemplate.ma
