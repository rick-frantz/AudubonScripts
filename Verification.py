##  Property of National Audubon Society
##  This script iterates through a series of folders in a directory and verifies any found GIS rasters are also in appropriate Esri file geodatabases (*.gdb)

import arcpy #import appropriate python libraries
import os
A = 0 #used for folder iteration

#List of folder names to iterate through
FolderName = [ 
"2000_suitability", "2000_suitability_kappa", 
"2020_suitability", "2020_suitability_kappa",
"2050_suitability", "2050_suitability_kappa",
"2080_suitability", "2080_suitability_kappa",
"2000_2020_consensus", "2000_2020_consensus_kappa", "2000_2020_difference", "2000_2020_difference_kappa",
"2000_2050_consensus", "2000_2050_consensus_kappa", "2000_2050_difference", "2000_2050_difference_kappa",
"2000_2080_consensus", "2000_2080_consensus_kappa", "2000_2080_difference", "2000_2080_difference_kappa" ]

WorkingFolder = "J:\\" #this is the directory where the above folders are located

#This sets up the iteration of the folders
for index in range(len(FolderName)):
	print FolderName[A]
	arcpy.env.workspace = WorkingFolder + "".join(FolderName[A]) #set the workspace for the rest of the logic

	# Start the Raster verification process
	rasterlist = arcpy.ListRasters("*" , "IMG") # the first parameter in the parenthesis is a filter for imported raster name and the second is for file type
	for raster in rasterlist:
		#Local Variables
		InRaster = raster
		InRasterPath = "J:\\" + FolderName[A] + "\\" +InRaster
		OutGDB = "Master.gdb" #set the default geodatabase
		CodeBird = InRaster[0:4] #this is the first 4 characters of the raster and the BBL abbreviation
		FilePrefix = "BirdCode" #set the default file prefix

		# Use the bird code to set the output geodatabase & file prefix
		if (CodeBird == "ACWO"):
			OutGDB = "E01087400_acorn_woodpecker.gdb"
			FilePrefix = "E01087400_acowoo"
		elif (CodeBird == "ACFL"):
			OutGDB = "E01457400_acadian_flycatcher.gdb"
			FilePrefix = "E01457400_acafly"
		elif (CodeBird =="ABDU"):
			OutGDB ="E00039000_american_black_duck.gdb"
			FilePrefix = "E00039000_ambduc"
		elif (CodeBird =="ABTO"):
			OutGDB ="E02963700_aberts_towhee.gdb"
			FilePrefix = "E02963700_abetow"
		elif (CodeBird =="AFCD"):
			OutGDB ="E00483100_african_collared_dove.gdb"
			FilePrefix = "E00483100_afcdov1"
		elif (CodeBird =="ALFL"):
			OutGDB ="E01457500_alder_flycatcher.gdb"
			FilePrefix = "E01457500_aldfly"
		elif (CodeBird =="ALHU"):
			OutGDB ="E00892600_allens_hummingbird.gdb"
			FilePrefix = "E00892600_allhum"
		elif (CodeBird =="ALOR"):
			OutGDB ="E03061700_altamira_oriole.gdb"
			FilePrefix = "E03061700_altori"
		elif (CodeBird =="AMAV"):
			OutGDB ="E00378200_american_avocet.gdb"
			FilePrefix = "E00378200_ameavo"
		elif (CodeBird =="AMBI"):
			OutGDB ="E00208100_american_bittern.gdb"
			FilePrefix = "E00208100_amebit"
		elif (CodeBird =="AMCO"):
			OutGDB ="E00361500_american_coot.gdb"
			FilePrefix = "E00361500_amecoo"
		elif (CodeBird =="AMCR"):
			OutGDB ="E01907300_american_crow.gdb"
			FilePrefix = "E01907300_amecro"
		elif (CodeBird =="AMDI"):
			OutGDB ="E02147500_american_dipper.gdb"
			FilePrefix = "E02147500_amedip"
		elif (CodeBird =="AMGO"):
			OutGDB ="E03103900_american_goldfinch.gdb"
			FilePrefix = "E03103900_amegfi"
		elif (CodeBird =="AMGP"):
			OutGDB ="E00380550_american_golden_plover.gdb"
			FilePrefix = "E00380550_amgplo"
		elif (CodeBird =="AMKE"):
			OutGDB ="E01158183_american_kestrel.gdb"
			FilePrefix = "E01158183_amekes"
		elif (CodeBird =="AMOY"):
			OutGDB ="E00379600_american_oystercatcher.gdb"
			FilePrefix = "E00379600_ameoys"
		elif (CodeBird =="AMPI"):
			OutGDB ="E02766900_american_pipit.gdb"
			FilePrefix = "E02766900_amepip"
		elif (CodeBird =="AMRE"):
			OutGDB ="E02786100_american_redstart.gdb"
			FilePrefix = "E02786100_amered"
		elif (CodeBird =="AMRO"):
			OutGDB ="E02490300_american_robin.gdb"
			FilePrefix = "E02490300_amerob"
		elif (CodeBird =="AMWI"):
			OutGDB ="E00038600_american_wigeon.gdb"
			FilePrefix = "E00038600_amewig"
		elif (CodeBird =="AMWO"):
			OutGDB ="E00413500_american_woodcock.gdb"
			FilePrefix = "E00413500_amewoo"
		elif (CodeBird =="ANHI"):
			OutGDB ="E00205600_anhinga.gdb"
			FilePrefix = "E00205600_anhing"
		elif (CodeBird =="ANHU"):
			OutGDB ="E00890600_annas_hummingbird.gdb"
			FilePrefix = "E00890600_annhum"
		elif (CodeBird =="ANMU"):
			OutGDB ="E00426261_ancient_murrelet.gdb"
			FilePrefix = "E00426261_ancmur"
		elif (CodeBird =="APFA"):
			OutGDB ="E01158241_aplomado_falcon.gdb"
			FilePrefix = "E01158241_aplfal"
		elif (CodeBird =="ARTE"):
			OutGDB ="E00449700_arctic_tern.gdb"
			FilePrefix = "E00449700_arcter"
		elif (CodeBird =="ARWA"):
			OutGDB ="E02204800_arctic_warbler.gdb"
			FilePrefix = "E02204800_arcwar"
		elif (CodeBird =="ARWO"):
			OutGDB ="E01118000_arizona_woodpecker.gdb"
			FilePrefix = "E01118000_ariwoo"
		elif (CodeBird =="ATFL"):
			OutGDB ="E01492100_ash_throated_flycatcher.gdb"
			FilePrefix = "E01492100_astfly"
		elif (CodeBird =="ATPU"):
			OutGDB ="E00426275_atlantic_puffin.gdb"
			FilePrefix = "E00426275_atlpuf"
		elif (CodeBird =="ATSP"):
			OutGDB ="E02970900_american_tree_sparrow.gdb"
			FilePrefix = "E02970900_amtspa"
		elif (CodeBird =="ATTW"):
			OutGDB ="E01119400_american_three_toed_woodpecker.gdb"
			FilePrefix = "E01119400_attwoo1"
		elif (CodeBird =="AUOR"):
			OutGDB ="E03062500_audubons_oriole.gdb"
			FilePrefix = "E03062500_audori"
		elif (CodeBird =="AWPE"):
			OutGDB ="E00206900_american_white_pelican.gdb"
			FilePrefix = "E00206900_amwpel"
		elif (CodeBird =="BACS"):
			OutGDB ="E02968000_bachmans_sparrow.gdb"
			FilePrefix = "E02968000_bacspa"
		elif (CodeBird =="BADO"):
			OutGDB ="E00752600_barred_owl.gdb"
			FilePrefix = "E00752600_brdowl"
		elif (CodeBird =="BAEA"):
			OutGDB ="E00288100_bald_eagle.gdb"
			FilePrefix = "E00288100_baleag"
		elif (CodeBird =="BAGO"):
			OutGDB ="E00054800_barrows_goldeneye.gdb"
			FilePrefix = "E00054800_bargol"
		elif (CodeBird =="BAIS"):
			OutGDB ="E02981100_bairds_sparrow.gdb"
			FilePrefix = "E02981100_baispa"
		elif (CodeBird =="BANO"):
			OutGDB ="E00698200_barn_owl.gdb"
			FilePrefix = "E00698200_brnowl"
		elif (CodeBird =="BANS"):
			OutGDB ="E01999600_bank_swallow.gdb"
			FilePrefix = "E01999600_banswa"
		elif (CodeBird =="BAOR"):
			OutGDB ="E03063200_baltimore_oriole.gdb"
			FilePrefix = "E03063200_balori"
		elif (CodeBird =="BARS"):
			OutGDB ="E02003700_barn_swallow.gdb"
			FilePrefix = "E02003700_barswa"
		elif (CodeBird =="BAWW"):
			OutGDB ="E02778200_black_and_white_warbler.gdb"
			FilePrefix = "E02778200_bawwar"
		elif (CodeBird =="BBCU"):
			OutGDB ="E00691100_black_billed_cuckoo.gdb"
			FilePrefix = "E00691100_bkbcuc"
		elif (CodeBird =="BBEH"):
			OutGDB ="E00918200_buff_bellied_hummingbird.gdb"
			FilePrefix = "E00918200_bubhum"
		elif (CodeBird =="BBIH"):
			OutGDB ="E00899200_broad_billed_hummingbird.gdb"
			FilePrefix = "E00899200_brbhum"
		elif (CodeBird =="BBMA"):
			OutGDB ="E01900000_black_billed_magpie.gdb"
			FilePrefix = "E01900000_bkbmag1"
		elif (CodeBird =="BBPL"):
			OutGDB ="E00380510_black_bellied_plover.gdb"
			FilePrefix = "E00380510_bkbplo"
		elif (CodeBird =="BBWA"):
			OutGDB ="E02788300_bay_breasted_warbler.gdb"
			FilePrefix = "E02788300_babwar"
		elif (CodeBird =="BBWD"):
			OutGDB ="E00021500_black_bellied_whistling_duck.gdb"
			FilePrefix = "E00021500_bbwduc"
		elif (CodeBird =="BBWO"):
			OutGDB ="E01119800_black_backed_woodpecker.gdb"
			FilePrefix = "E01119800_bkbwoo"
		elif (CodeBird =="BCCH"):
			OutGDB ="E02024600_black_capped_chickadee.gdb"
			FilePrefix = "E02024600_bkcchi"
		elif (CodeBird =="BCFL"):
			OutGDB ="E01492900_brown_crested_flycatcher.gdb"
			FilePrefix = "E01492900_bncfly"
		elif (CodeBird =="BCHU"):
			OutGDB ="E00889800_black_chinned_hummingbird.gdb"
			FilePrefix = "E00889800_bkchum"
		elif (CodeBird =="BCNH"):
			OutGDB ="E00223300_black_crowned_night_heron.gdb"
			FilePrefix = "E00223300_bcnher"
		elif (CodeBird =="BCRF"):
			OutGDB ="E03083500_brown_capped_rosy_finch.gdb"
			FilePrefix = "E03083500_bcrfin"
		elif (CodeBird =="BCSP"):
			OutGDB ="E02973000_black_chinned_sparrow.gdb"
			FilePrefix = "E02973000_bkcspa"
		elif (CodeBird =="BCTI"):
			OutGDB ="E02048600_black_crested_titmouse.gdb"
			FilePrefix = "E02048600_blctit4"
		elif (CodeBird =="BCVI"):
			OutGDB ="E01778400_black_capped_vireo.gdb"
			FilePrefix = "E01778400_bkcvir1"
		elif (CodeBird =="BEKI"):
			OutGDB ="E00993200_belted_kingfisher.gdb"
			FilePrefix = "E00993200_belkin1"
		elif (CodeBird =="BETH"):
			OutGDB ="E02640100_bendires_thrasher.gdb"
			FilePrefix = "E02640100_benthr"
		elif (CodeBird =="BEVI"):
			OutGDB ="E01777800_bells_vireo.gdb"
			FilePrefix = "E01777800_belvir"
		elif (CodeBird =="BEWR"):
			OutGDB ="E02133000_bewicks_wren.gdb"
			FilePrefix = "E02133000_bewwre"
		elif (CodeBird =="BGGN"):
			OutGDB ="E02140300_blue_gray_gnatcatcher.gdb"
			FilePrefix = "E02140300_buggna"
		elif (CodeBird =="BHCO"):
			OutGDB ="E03052100_brown_headed_cowbird.gdb"
			FilePrefix = "E03052100_bnhcow"
		elif (CodeBird =="BHGR"):
			OutGDB ="E03027500_black_headed_grosbeak.gdb"
			FilePrefix = "E03027500_bkhgro"
		elif (CodeBird =="BHGU"):
			OutGDB ="E00428800_black_headed_gull.gdb"
			FilePrefix = "E00428800_bkhgul"
		elif (CodeBird =="BHNU"):
			OutGDB ="E02078100_brown_headed_nuthatch.gdb"
			FilePrefix = "E02078100_bnhnut"
		elif (CodeBird =="BITH"):
			OutGDB ="E02460000_bicknells_thrush.gdb"
			FilePrefix = "E02460000_bicthr"
		elif (CodeBird =="BLBW"):
			OutGDB ="E02788400_blackburnian_warbler.gdb"
			FilePrefix = "E02788400_bkbwar"
		elif (CodeBird =="BLGR"):
			OutGDB ="E03031200_blue_grosbeak.gdb"
			FilePrefix = "E03031200_blugrb1"
		elif (CodeBird =="BLGU"):
			OutGDB ="E00426238_black_guillemot.gdb"
			FilePrefix = "E00426238_blkgui"
		elif (CodeBird =="BLJA"):
			OutGDB ="E01883100_blue_jay.gdb"
			FilePrefix = "E01883100_blujay"
		elif (CodeBird =="BLKI"):
			OutGDB ="E00426400_black_legged_kittiwake.gdb"
			FilePrefix = "E00426400_bklkit"
		elif (CodeBird =="BLOY"):
			OutGDB ="E00380300_black_oystercatcher.gdb"
			FilePrefix = "E00380300_blkoys"
		elif (CodeBird =="BLPH"):
			OutGDB ="E01462100_black_phoebe.gdb"
			FilePrefix = "E01462100_blkpho"
		elif (CodeBird =="BLPW"):
			OutGDB ="E02792400_blackpoll_warbler.gdb"
			FilePrefix = "E02792400_bkpwar"
		elif (CodeBird =="BLRA"):
			OutGDB ="E00329900_black_rail.gdb"
			FilePrefix = "E00329900_blkrai"
		elif (CodeBird =="BLRF"):
			OutGDB ="E03083400_black_rosy_finch.gdb"
			FilePrefix = "E03083400_bkrfin"
		elif (CodeBird =="BLSC"):
			OutGDB ="E00053700_black_scoter.gdb"
			FilePrefix = "E00053700_blksco2"
		elif (CodeBird =="BLSK"):
			OutGDB ="E00453900_black_skimmer.gdb"
			FilePrefix = "E00453900_blkski"
		elif (CodeBird =="BLSW"):
			OutGDB ="E00804300_black_swift.gdb"
			FilePrefix = "E00804300_blkswi"
		elif (CodeBird =="BLTE"):
			OutGDB ="E00446500_black_tern.gdb"
			FilePrefix = "E00446500_blkter"
		elif (CodeBird =="BLTU"):
			OutGDB ="E00402600_black_turnstone.gdb"
			FilePrefix = "E00402600_blktur"
		elif (CodeBird =="BLVU"):
			OutGDB ="E00235800_black_vulture.gdb"
			FilePrefix = "E00235800_blkvul"
		elif (CodeBird =="BNST"):
			OutGDB ="E00377300_black_necked_stilt.gdb"
			FilePrefix = "E00377300_bknsti"
		elif (CodeBird =="BOBO"):
			OutGDB ="E03033800_bobolink.gdb"
			FilePrefix = "E03033800_boboli"
		elif (CodeBird =="BOCH"):
			OutGDB ="E02027900_boreal_chickadee.gdb"
			FilePrefix = "E02027900_borchi2"
		elif (CodeBird =="BOGU"):
			OutGDB ="E00427600_bonapartes_gull.gdb"
			FilePrefix = "E00427600_bongul"
		elif (CodeBird =="BOOW"):
			OutGDB ="E00759500_boreal_owl.gdb"
			FilePrefix = "E00759500_borowl"
		elif (CodeBird =="BOSP"):
			OutGDB ="E02966500_botteris_sparrow.gdb"
			FilePrefix = "E02966500_botspa"
		elif (CodeBird =="BOWA"):
			OutGDB ="E02773400_bohemian_waxwing.gdb"
			FilePrefix = "E02773400_bohwax"
		elif (CodeBird =="BRAC"):
			OutGDB ="E00198400_brandts_cormorant.gdb"
			FilePrefix = "E00198400_bracor"
		elif (CodeBird =="BRAN"):
			OutGDB ="E00026100_brant.gdb"
			FilePrefix = "E00026100_brant"
		elif (CodeBird =="BRBL"):
			OutGDB ="E03041900_brewers_blackbird.gdb"
			FilePrefix = "E03041900_brebla"
		elif (CodeBird =="BRCR"):
			OutGDB ="E02084600_brown_creeper.gdb"
			FilePrefix = "E02084600_brncre"
		elif (CodeBird =="BROC"):
			OutGDB ="E03051500_bronzed_cowbird.gdb"
			FilePrefix = "E03051500_brocow"
		elif (CodeBird =="BRPE"):
			OutGDB ="E00207000_brown_pelican.gdb"
			FilePrefix = "E00207000_brnpel"
		elif (CodeBird =="BRSP"):
			OutGDB ="E02972200_brewers_sparrow.gdb"	
			FilePrefix = "E02972200_brespa"
		elif (CodeBird =="BRTH"):	
			OutGDB ="E02639300_brown_thrasher.gdb"
			FilePrefix = "E02639300_brnthr"
		elif (CodeBird =="BRTI"):
			OutGDB ="E02047000_bridled_titmouse.gdb"
			FilePrefix = "E02047000_britit"
		elif (CodeBird =="BTAH"):
			OutGDB ="E00892200_broad_tailed_hummingbird.gdb"
			FilePrefix = "E00892200_brthum"
		elif (CodeBird =="BTBW"):
			OutGDB ="E02792600_black_throated_blue_warbler.gdb"
			FilePrefix = "E02792600_btbwar"
		elif (CodeBird =="BTGN"):
			OutGDB ="E02141500_black_tailed_gnatcatcher.gdb"
			FilePrefix = "E02141500_bktgna"
		elif (CodeBird =="BTGR"):
			OutGDB ="E03042600_boat_tailed_grackle.gdb"
			FilePrefix = "E03042600_botgra"
		elif (CodeBird =="BTHH"):
			OutGDB ="E00884000_blue_throated_hummingbird.gdb"
			FilePrefix = "E00884000_buthum"
		elif (CodeBird =="BTNW"):
			OutGDB ="E02797700_black_throated_green_warbler.gdb"
			FilePrefix = "E02797700_btnwar"
		elif (CodeBird =="BTPI"):
			OutGDB ="E00477800_band_tailed_pigeon.gdb"
			FilePrefix = "E00477800_batpig1"
		elif (CodeBird =="BTSP"):
			OutGDB ="E02974300_black_throated_sparrow.gdb"
			FilePrefix = "E02974300_bktspa"
		elif (CodeBird =="BTYW"):
			OutGDB ="E02796800_black_throated_gray_warbler.gdb"
			FilePrefix = "E02796800_btywar"
		elif (CodeBird =="BUFF"):
			OutGDB ="E00054100_bufflehead.gdb"
			FilePrefix = "E00054100_buffle"
		elif (CodeBird =="BUOR"):
			OutGDB ="E03060000_bullocks_oriole.gdb"
			FilePrefix = "E03060000_bulori"
		elif (CodeBird =="BUOW"):
			OutGDB ="E00742900_burrowing_owl.gdb"
			FilePrefix = "E00742900_burowl"
		elif (CodeBird =="BUSH"):
			OutGDB ="E02070800_bushtit.gdb"
			FilePrefix = "E02070800_bushti"
		elif (CodeBird =="BVSH"):
			OutGDB ="E00183000_black_vented_shearwater.gdb"
			FilePrefix = "E00183000_bkvshe"
		elif (CodeBird =="BWHA"):
			OutGDB ="E00296600_broad_winged_hawk.gdb"
			FilePrefix = "E00296600_brwhaw"
		elif (CodeBird =="BWTE"):
			OutGDB ="E00042300_blue_winged_teal.gdb"
			FilePrefix = "E00042300_buwtea"
		elif (CodeBird =="BWVI"):
			OutGDB ="E01786800_black_whiskered_vireo.gdb"
			FilePrefix = "E01786800_bkwvir"
		elif (CodeBird =="BWWA"):
			OutGDB ="E02777700_blue_winged_warbler.gdb"
			FilePrefix = "E02777700_buwwar"
		elif (CodeBird =="CAAU"):
			OutGDB ="E00426266_cassins_auklet.gdb"
			FilePrefix = "E00426266_casauk"
		elif (CodeBird =="CACG"):
			OutGDB ="E00028800_cackling_canada_goose.gdb"
			FilePrefix = "E00028800_y00470"
		elif (CodeBird =="CACH"):
			OutGDB ="E02024000_carolina_chickadee.gdb"
			FilePrefix = "E02024000_carchi"
		elif (CodeBird =="CACW"):
			OutGDB ="E02134550_cactus_wren.gdb"
			FilePrefix = "E02134550_cacwre"
		elif (CodeBird =="CAEG"):
			OutGDB ="E00218300_cattle_egret.gdb"
			FilePrefix = "E00218300_categr"
		elif (CodeBird =="CAFI"):
			OutGDB ="E03087890_cassins_finch.gdb"
			FilePrefix = "E03087890_casfin"
		elif (CodeBird =="CAGN"):
			OutGDB ="E02141400_california_gnatcatcher.gdb"
			FilePrefix = "E02141400_calgna"
		elif (CodeBird =="CAGU"):
			OutGDB ="E00432500_california_gull.gdb"
			FilePrefix = "E00432500_calgul"
		elif (CodeBird =="CAHU"):
			OutGDB ="E00894600_calliope_hummingbird.gdb"
			FilePrefix = "E00894600_calhum"
		elif (CodeBird =="CAKI"):
			OutGDB ="E01504500_cassins_kingbird.gdb"
			FilePrefix = "E01504500_caskin"
		elif (CodeBird =="CALT"):
			OutGDB ="E02962800_california_towhee.gdb"
			FilePrefix = "E02962800_caltow"
		elif (CodeBird =="CANT"):
			OutGDB ="E02962400_canyon_towhee.gdb"
			FilePrefix = "E02962400_cantow"
		elif (CodeBird =="CANV"):
			OutGDB ="E00049600_canvasback.gdb"
			FilePrefix = "E00049600_canvas"
		elif (CodeBird =="CANW"):
			OutGDB ="E02090400_canyon_wren.gdb"
			FilePrefix = "E02090400_canwre"
		elif (CodeBird =="CAQU"):
			OutGDB ="E00078600_california_quail.gdb"
			FilePrefix = "E00078600_calqua"
		elif (CodeBird =="CARW"):
			OutGDB ="E02131900_carolina_wren.gdb"
			FilePrefix = "E02131900_carwre"
		elif (CodeBird =="CASP"):
			OutGDB ="E02967400_cassins_sparrow.gdb"
			FilePrefix = "E02967400_casspa"
		elif (CodeBird =="CASW"):
			OutGDB ="E02012800_cave_swallow.gdb"
			FilePrefix = "E02012800_cavswa"
		elif (CodeBird =="CATE"):
			OutGDB ="E00446300_caspian_tern.gdb"
			FilePrefix = "E00446300_caster1"
		elif (CodeBird =="CATH"):
			OutGDB ="E02640900_california_thrasher.gdb"
			FilePrefix = "E02640900_calthr"
		elif (CodeBird =="CAWA"):
			OutGDB ="E02809000_canada_warbler.gdb"
			FilePrefix = "E02809000_canwar"
		elif (CodeBird =="CBCH"):
			OutGDB ="E02027500_chestnut_backed_chickadee.gdb"
			FilePrefix = "E02027500_chbchi"
		elif (CodeBird =="CBTH"):
			OutGDB ="E02638000_curve_billed_thrasher.gdb"
			FilePrefix = "E02638000_cubthr"
		elif (CodeBird =="CCLO"):
			OutGDB ="E02776400_chestnut_collared_longspur.gdb"
			FilePrefix = "E02776400_chclon"
		elif (CodeBird =="CCSP"):
			OutGDB ="E02971900_clay_colored_sparrow.gdb"
			FilePrefix = "E02971900_clcspa"
		elif (CodeBird =="CEDW"):
			OutGDB ="E02773800_cedar_waxwing.gdb"
			FilePrefix = "E02773800_cedwax"
		elif (CodeBird =="CERW"):
			OutGDB ="E02786400_cerulean_warbler.gdb"
			FilePrefix = "E02786400_cerwar"
		elif (CodeBird =="CHRA"):
			OutGDB ="E01908900_chihuahuan_raven.gdb"
			FilePrefix = "E01908900_chirav"
		elif (CodeBird =="CHSP"):
			OutGDB ="E02971200_chipping_sparrow.gdb"
			FilePrefix = "E02971200_chispa"
		elif (CodeBird =="CHSW"):
			OutGDB ="E00809600_chimney_swift.gdb"
			FilePrefix = "E00809600_chiswi"
		elif (CodeBird =="CHUK"):
			OutGDB ="E00093200_chukar.gdb"
			FilePrefix = "E00093200_chukar"
		elif (CodeBird =="CITE"):
			OutGDB ="E00042600_cinnamon_teal.gdb"
			FilePrefix = "E00042600_cintea"
		elif (CodeBird =="CLGR"):
			OutGDB ="E00163700_clarks_grebe.gdb"
			FilePrefix = "E00163700_clagre"
		elif (CodeBird =="CLNU"):
			OutGDB ="E01900700_clarks_nutcracker.gdb"
			FilePrefix = "E01900700_clanut"
		elif (CodeBird =="CLRA"):
			OutGDB ="E00337100_clapper_rail.gdb"
			FilePrefix = "E00337100_clarai"
		elif (CodeBird =="CLSW"):
			OutGDB ="E02012200_cliff_swallow.gdb"
			FilePrefix = "E02012200_cliswa"
		elif (CodeBird =="CMWA"):
			OutGDB ="E02786300_cape_may_warbler.gdb"
			FilePrefix = "E02786300_camwar"
		elif (CodeBird =="COEI"):
			OutGDB ="E00051700_common_eider.gdb"
			FilePrefix = "E00051700_comeid"
		elif (CodeBird =="COFL"):
			OutGDB ="E01460400_cordilleran_flycatcher.gdb"
			FilePrefix = "E01460400_corfly"
		elif (CodeBird =="COGA"):
			OutGDB ="E00358350_common_gallinule.gdb"
			FilePrefix = "E00358350_comgal1"
		elif (CodeBird =="COGD"):
			OutGDB ="E00502500_common_ground_dove.gdb"
			FilePrefix = "E00502500_cogdov"
		elif (CodeBird =="COGO"):
			OutGDB ="E00054300_common_goldeneye.gdb"
			FilePrefix = "E00054300_comgol"
		elif (CodeBird =="COGR"):
			OutGDB ="E03042100_common_grackle.gdb"
			FilePrefix = "E03042100_comgra"
		elif (CodeBird =="COHA"):
			OutGDB ="E00282100_coopers_hawk.gdb"
			FilePrefix = "E00282100_coohaw"
		elif (CodeBird =="COHU"):
			OutGDB ="E00891400_costas_hummingbird.gdb"
			FilePrefix = "E00891400_coshum"
		elif (CodeBird =="COKI"):
			OutGDB ="E01504200_couchs_kingbird.gdb"
			FilePrefix = "E01504200_coukin"
		elif (CodeBird =="COLO"):
			OutGDB ="E00156700_common_loon.gdb"
			FilePrefix = "E00156700_comloo"
		elif (CodeBird =="COME"):
			OutGDB ="E00055500_common_merganser.gdb"
			FilePrefix = "E00055500_commer"
		elif (CodeBird =="COMU"):
			OutGDB ="E00426222_common_murre.gdb"
			FilePrefix = "E00426222_commur"
		elif (CodeBird =="COMY"):
			OutGDB ="E02659400_common_myna.gdb"
			FilePrefix = "E02659400_commyn"
		elif (CodeBird =="CONI"):
			OutGDB ="E00777500_common_nighthawk.gdb"
			FilePrefix = "E00777500_comnig"
		elif (CodeBird =="CONW"):
			OutGDB ="E02780700_connecticut_warbler.gdb"
			FilePrefix = "E02780700_conwar"
		elif (CodeBird =="COPA"):
			OutGDB ="E00781300_common_pauraque.gdb"
			FilePrefix = "E00781300_compau"
		elif (CodeBird =="COPO"):
			OutGDB ="E00786200_common_poorwill.gdb"
			FilePrefix = "E00786200_compoo"
		elif (CodeBird =="CORA"):
			OutGDB ="E01913400_common_raven.gdb"
			FilePrefix = "E01913400_comrav"
		elif (CodeBird =="CORE"):
			OutGDB ="E03100900_common_redpoll.gdb"
			FilePrefix = "E03100900_comred"
		elif (CodeBird =="COTE"):
			OutGDB ="E00449200_common_tern.gdb"
			FilePrefix = "E00449200_comter"
		elif (CodeBird =="COYE"):
			OutGDB ="E02783800_common_yellowthroat.gdb"
			FilePrefix = "E02783800_comyel"
		elif (CodeBird =="CRCA"):
			OutGDB ="E01158124_crested_caracara.gdb"
			FilePrefix = "E01158124_crecar1"
		elif (CodeBird =="CRTH"):
			OutGDB ="E02641700_crissal_thrasher.gdb"
			FilePrefix = "E02641700_crithr"
		elif (CodeBird =="CSWA"):
			OutGDB ="E02792300_chestnut_sided_warbler.gdb"
			FilePrefix = "E02792300_chswar"
		elif (CodeBird =="CWWI"):
			OutGDB ="E00786750_chuck_wills_widow.gdb"
			FilePrefix = "E00786750_chwwid"
		elif (CodeBird =="DCCO"):
			OutGDB ="E00198800_double_crested_cormorant.gdb"
			FilePrefix = "E00198800_doccor"
		elif (CodeBird =="DCFL"):
			OutGDB ="E01488700_dusky_capped_flycatcher.gdb"
			FilePrefix = "E01488700_ducfly"
		elif (CodeBird =="DEJU"):
			OutGDB ="E02995800_dark_eyed_junco.gdb"
			FilePrefix = "E02995800_daejun"
		elif (CodeBird =="DICK"):
			OutGDB ="E03033700_dickcissel.gdb"
			FilePrefix = "E03033700_dickci"
		elif (CodeBird =="DOVE"):
			OutGDB ="E00426219_dovekie.gdb"
			FilePrefix = "E00426219_doveki"
		elif (CodeBird =="DOWO"):
			OutGDB ="E01114800_downy_woodpecker.gdb"
			FilePrefix = "E01114800_dowwoo"
		elif (CodeBird =="DUFL"):
			OutGDB ="E01459100_dusky_flycatcher.gdb"
			FilePrefix = "E01459100_dusfly"
		elif (CodeBird =="DUGR"):
			OutGDB ="E00153900_dusky_sooty_grouse.gdb"
			FilePrefix = "E00153900_blugrs"
		elif (CodeBird =="DUNL"):
			OutGDB ="E00406000_dunlin.gdb"
			FilePrefix = "E00406000_dunlin"
		elif (CodeBird =="EABL"):
			OutGDB ="E02448200_eastern_bluebird.gdb"
			FilePrefix = "E02448200_easblu"
		elif (CodeBird =="EAGR"):
			OutGDB ="E00162100_eared_grebe.gdb"
			FilePrefix = "E00162100_eargre"
		elif (CodeBird =="EAKI"):
			OutGDB ="E01505500_eastern_kingbird.gdb"
			FilePrefix = "E01505500_easkin"
		elif (CodeBird =="EAME"):
			OutGDB ="E03038700_eastern_meadowlark.gdb"
			FilePrefix = "E03038700_easmea"
		elif (CodeBird =="EAPH"):
			OutGDB ="E01463200_eastern_phoebe.gdb"
			FilePrefix = "E01463200_easpho"
		elif (CodeBird =="EASO"):
			OutGDB ="E00716000_eastern_screech_owl.gdb"
			FilePrefix = "E00716000_easowl1"
		elif (CodeBird =="EATO"):
			OutGDB ="E02960600_eastern_towhee.gdb"
			FilePrefix = "E02960600_eastow"
		elif (CodeBird =="EAWP"):
			OutGDB ="E01453400_eastern_wood_pewee.gdb"
			FilePrefix = "E01453400_eawpew"
		elif (CodeBird =="ELTR"):
			OutGDB ="E00940200_elegant_trogon.gdb"
			FilePrefix = "E00940200_eletro"
		elif (CodeBird =="EMGO"):
			OutGDB ="E00025300_emperor_goose.gdb"
			FilePrefix = "E00025300_empgoo"
		elif (CodeBird =="ETSP"):
			OutGDB ="E03140300_eurasian_tree_sparrow.gdb"
			FilePrefix = "E03140300_eutspa"
		elif (CodeBird =="EUCD"):
			OutGDB ="E00482800_eurasian_collared_dove.gdb"
			FilePrefix = "E00482800_eucdov"
		elif (CodeBird =="EUST"):
			OutGDB ="E02662100_european_starling.gdb"
			FilePrefix = "E02662100_eursta"
		elif (CodeBird =="EUWI"):
			OutGDB ="E00038400_eurasian_wigeon.gdb"
			FilePrefix = "E00038400_eurwig"
		elif (CodeBird =="EVGR"):
			OutGDB ="E03127300_evening_grosbeak.gdb"
			FilePrefix = "E03127300_evegro"
		elif (CodeBird =="EWPW"):
			OutGDB ="E00791200_eastern_whip_poor_will.gdb"
			FilePrefix = "E00791200_whipp1"
		elif (CodeBird =="EYWA"):
			OutGDB ="E02749500_eastern_yellow_wagtail.gdb"
			FilePrefix = "E02749500_eaywag"
		elif (CodeBird =="FEHA"):
			OutGDB ="E00300600_ferruginous_hawk.gdb"
			FilePrefix = "E00300600_ferhaw"
		elif (CodeBird =="FEPO"):
			OutGDB ="E00737500_ferruginous_pygmy_owl.gdb"
			FilePrefix = "E00737500_fepowl"
		elif (CodeBird =="FICR"):
			OutGDB ="E01908700_fish_crow.gdb"
			FilePrefix = "E01908700_fiscro"
		elif (CodeBird =="FISP"):
			OutGDB ="E02972600_field_sparrow.gdb"
			FilePrefix = "E02972600_fiespa"
		elif (CodeBird =="FLSJ"):
			OutGDB ="E01883700_florida_scrub_jay.gdb"
			FilePrefix = "E01883700_flsjay"
		elif (CodeBird =="FOSP"):
			OutGDB ="E02984000_fox_sparrow.gdb"
			FilePrefix = "E02984000_foxspa"
		elif (CodeBird =="FOTE"):
			OutGDB ="E00450800_forsters_tern.gdb"
			FilePrefix = "E00450800_forter"
		elif (CodeBird =="FRGU"):
			OutGDB ="E00429900_franklins_gull.gdb"
			FilePrefix = "E00429900_fragul"
		elif (CodeBird =="FSSP"):
			OutGDB ="E02974200_five_striped_sparrow.gdb"
			FilePrefix = "E02974200_fisspa"
		elif (CodeBird =="FUWD"):
			OutGDB ="E00021700_fulvous_whistling_duck.gdb"
			FilePrefix = "E00021700_fuwduc"
		elif (CodeBird =="GADW"):
			OutGDB ="E00037700_gadwall.gdb"
			FilePrefix = "E00037700_gadwal"
		elif (CodeBird =="GAQU"):
			OutGDB ="E00079600_gambels_quail.gdb"
			FilePrefix = "E00079600_gamqua"
		elif (CodeBird =="GBAN"):
			OutGDB ="E00695100_groove_billed_ani.gdb"
			FilePrefix = "E00695100_grbani"
		elif (CodeBird =="GBBG"):
			OutGDB ="E00437100_great_black_backed_gull.gdb"
			FilePrefix = "E00437100_gbbgul"
		elif (CodeBird =="GBHE"):
			OutGDB ="E00211800_great_blue_heron.gdb"
			FilePrefix = "E00211800_grbher3"
		elif (CodeBird =="GBTE"):
			OutGDB ="E00445600_gull_billed_tern.gdb"
			FilePrefix = "E00445600_gubter1"
		elif (CodeBird =="GCFL"):
			OutGDB ="E01492800_great_crested_flycatcher.gdb"
			FilePrefix = "E01492800_grcfly"
		elif (CodeBird =="GCKI"):
			OutGDB ="E02193200_golden_crowned_kinglet.gdb"
			FilePrefix = "E02193200_gockin"
		elif (CodeBird =="GCRF"):
			OutGDB ="E03082500_gray_crowned_rosy_finch.gdb"
			FilePrefix = "E03082500_gcrfin"
		elif (CodeBird =="GCSP"):
			OutGDB ="E02995500_golden_crowned_sparrow.gdb"
			FilePrefix = "E02995500_gocspa"
		elif (CodeBird =="GCTH"):
			OutGDB ="E02459700_gray_cheeked_thrush.gdb"
			FilePrefix = "E02459700_gycthr"
		elif (CodeBird =="GCWA"):
			OutGDB ="E02797600_golden_cheeked_warbler.gdb"
			FilePrefix = "E02797600_gchwar"
		elif (CodeBird =="GFWO"):
			OutGDB ="E01090900_golden_fronted_woodpecker.gdb"
			FilePrefix = "E01090900_gofwoo"
		elif (CodeBird =="GGOW"):
			OutGDB ="E00754700_great_gray_owl.gdb"
			FilePrefix = "E00754700_grgowl"
		elif (CodeBird =="GHOW"):
			OutGDB ="E00725400_great_horned_owl.gdb"
			FilePrefix = "E00725400_grhowl"
		elif (CodeBird =="GIFL"):
			OutGDB ="E01132100_gilded_flicker.gdb"
			FilePrefix = "E01132100_gilfli"
		elif (CodeBird =="GIWO"):
			OutGDB ="E01090400_gila_woodpecker.gdb"
			FilePrefix = "E01090400_gilwoo"
		elif (CodeBird =="GKIN"):
			OutGDB ="E00993900_green_kingfisher.gdb"
			FilePrefix = "E00993900_grnkin"
		elif (CodeBird =="GKIS"):
			OutGDB ="E01495800_great_kiskadee.gdb"
			FilePrefix = "E01495800_grekis"
		elif (CodeBird =="GLGU"):
			OutGDB ="E00436500_glaucous_gull.gdb"
			FilePrefix = "E00436500_glagul"
		elif (CodeBird =="GLIB"):
			OutGDB ="E00226800_glossy_ibis.gdb"
			FilePrefix = "E00226800_gloibi"
		elif (CodeBird =="GOEA"):
			OutGDB ="E00258800_golden_eagle.gdb"
			FilePrefix = "E00258800_goleag"
		elif (CodeBird =="GRAJ"):
			OutGDB ="E01872200_gray_jay.gdb"
			FilePrefix = "E01872200_gryjay"
		elif (CodeBird =="GRAK"):
			OutGDB ="E01505600_gray_kingbird.gdb"
			FilePrefix = "E01505600_grykin"
		elif (CodeBird =="GRAP"):
			OutGDB ="E00107600_gray_partridge.gdb"
			FilePrefix = "E00107600_grypar"
		elif (CodeBird =="GRCA"):
			OutGDB ="E02635800_gray_catbird.gdb"
			FilePrefix = "E02635800_grycat"
		elif (CodeBird =="GRCO"):
			OutGDB ="E00199600_great_cormorant.gdb"
			FilePrefix = "E00199600_grecor"
		elif (CodeBird =="GREG"):
			OutGDB ="E00214400_great_egret.gdb"
			FilePrefix = "E00214400_greegr"
		elif (CodeBird =="GREJ"):
			OutGDB ="E01877200_green_jay.gdb"	
			FilePrefix = "E01877200_grnjay"
		elif (CodeBird =="GREP"):
			OutGDB ="E01158955_green_parakeet.gdb"
			FilePrefix = "E01158955_grnpar"
		elif (CodeBird =="GRFL"):
			OutGDB ="E01459000_gray_flycatcher.gdb"
			FilePrefix = "E01459000_gryfly"
		elif (CodeBird =="GRHA"):
			OutGDB ="E00297400_gray_hawk.gdb"
			FilePrefix = "E00297400_gryhaw2"
		elif (CodeBird =="GRHE"):
			OutGDB ="E00219600_green_heron.gdb"
			FilePrefix = "E00219600_grnher"
		elif (CodeBird =="GRPC"):
			OutGDB ="E00154800_greater_prairie_chicken.gdb"
			FilePrefix = "E00154800_grpchi"
		elif (CodeBird =="GRPE"):
			OutGDB ="E01451700_greater_pewee.gdb"
			FilePrefix = "E01451700_grepew"
		elif (CodeBird =="GRRO"):
			OutGDB ="E00693600_greater_roadrunner.gdb"
			FilePrefix = "E00693600_greroa"
		elif (CodeBird =="GRSC"):
			OutGDB ="E00050800_greater_scaup.gdb"
			FilePrefix = "E00050800_gresca"
		elif (CodeBird =="GRSG"):
			OutGDB ="E00145800_greater_sage_grouse.gdb"
			FilePrefix = "E00145800_saggro"
		elif (CodeBird =="GRSP"):
			OutGDB ="E02978800_grasshopper_sparrow.gdb"
			FilePrefix = "E02978800_graspa"
		elif (CodeBird =="GRVI"):
			OutGDB ="E01778600_gray_vireo.gdb"
			FilePrefix = "E01778600_gryvir"
		elif (CodeBird =="GRWA"):
			OutGDB ="E02796200_graces_warbler.gdb"
			FilePrefix = "E02796200_grawar"
		elif (CodeBird =="GRYE"):
			OutGDB ="E00397100_greater_yellowlegs.gdb"
			FilePrefix = "E00397100_greyel"
		elif (CodeBird =="GTGR"):
			OutGDB ="E03043200_great_tailed_grackle.gdb"
			FilePrefix = "E03043200_grtgra"
		elif (CodeBird =="GTTO"):
			OutGDB ="E02957200_green_tailed_towhee.gdb"
			FilePrefix = "E02957200_gnttow"
		elif (CodeBird =="GWFG"):
			OutGDB ="E00023700_greater_white_fronted_goose.gdb"
			FilePrefix = "E00023700_gwfgoo"
		elif (CodeBird =="GWGU"):
			OutGDB ="E00436300_glaucous_winged_gull.gdb"
			FilePrefix = "E00436300_glwgul"
		elif (CodeBird =="GWHE"):
			OutGDB ="E00212300_great_blue_heron_white_form.gdb"
			FilePrefix = "E00212300_grwher"
		elif (CodeBird =="GWTE"):
			OutGDB ="E00046200_green_winged_teal.gdb"
			FilePrefix = "E00046200_gnwtea"
		elif (CodeBird =="GWWA"):
			OutGDB ="E02778100_golden_winged_warbler.gdb"
			FilePrefix = "E02778100_gowwar"
		elif (CodeBird =="GYRF"):
			OutGDB ="E01158260_gyrfalcon.gdb"
			FilePrefix = "E01158260_gyrfal"
		elif (CodeBird =="HADU"):
			OutGDB ="E00052600_harlequin_duck.gdb"
			FilePrefix = "E00052600_harduc"
		elif (CodeBird =="HAFL"):
			OutGDB ="E01458900_hammonds_flycatcher.gdb"
			FilePrefix = "E01458900_hamfly"
		elif (CodeBird =="HASH"):
			OutGDB ="E00293400_harriss_hawk.gdb"
			FilePrefix = "E00293400_hrshaw"
		elif (CodeBird =="HASP"):
			OutGDB ="E02994500_harriss_sparrow.gdb"
			FilePrefix = "E02994500_harspa"
		elif (CodeBird =="HAWO"):
			OutGDB ="E01116400_hairy_woodpecker.gdb"
			FilePrefix = "E01116400_haiwoo"
		elif (CodeBird =="HBKI"):
			OutGDB ="E00240900_hook_billed_kite.gdb"
			FilePrefix = "E00240900_hobkit"
		elif (CodeBird =="HEEG"):
			OutGDB ="E00431300_heermanns_gull.gdb"
			FilePrefix = "E00431300_heegul"
		elif (CodeBird =="HERG"):
			OutGDB ="E00432800_herring_gull.gdb"
			FilePrefix = "E00432800_hergul"
		elif (CodeBird =="HESP"):
			OutGDB ="E02981200_henslows_sparrow.gdb"
			FilePrefix = "E02981200_henspa"
		elif (CodeBird =="HETA"):
			OutGDB ="E03014100_hepatic_tanager.gdb"
			FilePrefix = "E03014100_heptan"
		elif (CodeBird =="HETH"):
			OutGDB ="E02460800_hermit_thrush.gdb"
			FilePrefix = "E02460800_herthr"
		elif (CodeBird =="HEWA"):
			OutGDB ="E02797300_hermit_warbler.gdb"
			FilePrefix = "E02797300_herwar"
		elif (CodeBird =="HOFI"):
			OutGDB ="E03086600_house_finch.gdb"
			FilePrefix = "E03086600_houfin"
		elif (CodeBird =="HOGR"):
			OutGDB ="E00161100_horned_grebe.gdb"
			FilePrefix = "E00161100_horgre"
		elif (CodeBird =="HOLA"):
			OutGDB ="E01987000_horned_lark.gdb"
			FilePrefix = "E01987000_horlar"
		elif (CodeBird =="HOME"):
			OutGDB ="E00055300_hooded_merganser.gdb"
			FilePrefix = "E00055300_hoomer"
		elif (CodeBird =="HOOR"):
			OutGDB ="E03054900_hooded_oriole.gdb"
			FilePrefix = "E03054900_hooori"
		elif (CodeBird =="HORE"):
			OutGDB ="E03101600_hoary_redpoll.gdb"
			FilePrefix = "E03101600_hoared"
		elif (CodeBird =="HOSP"):
			OutGDB ="E03134500_house_sparrow.gdb"
			FilePrefix = "E03134500_houspa"
		elif (CodeBird =="HOWA"):
			OutGDB ="E02786000_hooded_warbler.gdb"
			FilePrefix = "E02786000_hoowar"
		elif (CodeBird =="HOWR"):
			OutGDB ="E02113800_house_wren.gdb"
			FilePrefix = "E02113800_houwre"
		elif (CodeBird =="HUGO"):
			OutGDB ="E00401400_hudsonian_godwit.gdb"
			FilePrefix = "E00401400_hudgod"
		elif (CodeBird =="HUVI"):
			OutGDB ="E01780700_huttons_vireo.gdb"
			FilePrefix = "E01780700_hutvir"
		elif (CodeBird =="ICGU"):
			OutGDB ="E00435100_iceland_gull.gdb"
			FilePrefix = "E00435100_icegul"
		elif (CodeBird =="INBU"):
			OutGDB ="E03032200_indigo_bunting.gdb"
			FilePrefix = "E03032200_indbun"
		elif (CodeBird =="INDO"):
			OutGDB ="E00502400_inca_dove.gdb"
			FilePrefix = "E00502400_incdov"
		elif (CodeBird =="JUTI"):
			OutGDB ="E02048000_juniper_titmouse.gdb"
			FilePrefix = "E02048000_juntit1"
		elif (CodeBird =="KEWA"):
			OutGDB ="E02782500_kentucky_warbler.gdb"
			FilePrefix = "E02782500_kenwar"
		elif (CodeBird =="KIEI"):
			OutGDB ="E00051600_king_eider.gdb"
			FilePrefix = "E00051600_kineid"
		elif (CodeBird =="KILL"):
			OutGDB ="E00392100_killdeer.gdb"
			FilePrefix = "E00392100_killde"
		elif (CodeBird =="KIMU"):
			OutGDB ="E00426255_kittlitzs_murrelet.gdb"
			FilePrefix = "E00426255_kitmur"
		elif (CodeBird =="KIRA"):
			OutGDB ="E00339500_king_rail.gdb"
			FilePrefix = "E00339500_kinrai"
		elif (CodeBird =="LAGO"):
			OutGDB ="E03103800_lawrences_goldfinch.gdb"
			FilePrefix = "E03103800_lawgol"
		elif (CodeBird =="LAGU"):
			OutGDB ="E00429500_laughing_gull.gdb"
			FilePrefix = "E00429500_laugul"
		elif (CodeBird =="LALO"):
			OutGDB ="E02776350_lapland_longspur.gdb"
			FilePrefix = "E02776350_laplon"
		elif (CodeBird =="LARB"):
			OutGDB ="E02976100_lark_bunting.gdb"
			FilePrefix = "E02976100_larbun"
		elif (CodeBird =="LASP"):
			OutGDB ="E02974000_lark_sparrow.gdb"
			FilePrefix = "E02974000_larspa"
		elif (CodeBird =="LAZB"):
			OutGDB ="E03032000_lazuli_bunting.gdb"
			FilePrefix = "E03032000_lazbun"
		elif (CodeBird =="LBBG"):
			OutGDB ="E00435500_lesser_black_backed_gull.gdb"
			FilePrefix = "E00435500_lbbgul"
		elif (CodeBird =="LBCU"):
			OutGDB ="E00400600_long_billed_curlew.gdb"
			FilePrefix = "E00400600_lobcur"
		elif (CodeBird =="LBDO"):
			OutGDB ="E00408400_long_billed_dowitcher.gdb"
			FilePrefix = "E00408400_lobdow"
		elif (CodeBird =="LBHE"):
			OutGDB ="E00217300_little_blue_heron.gdb"
			FilePrefix = "E00217300_libher"
		elif (CodeBird =="LBTH"):
			OutGDB ="E02639600_long_billed_thrasher.gdb"
			FilePrefix = "E02639600_lobthr"
		elif (CodeBird =="LBWO"):
			OutGDB ="E01113700_ladder_backed_woodpecker.gdb"
			FilePrefix = "E01113700_labwoo"
		elif (CodeBird =="LCSP"):
			OutGDB ="E02981500_le_contes_sparrow.gdb"
			FilePrefix = "E02981500_lecspa"
		elif (CodeBird =="LCTH"):
			OutGDB ="E02641200_le_contes_thrasher.gdb"
			FilePrefix = "E02641200_lecthr"
		elif (CodeBird =="LEBI"):
			OutGDB ="E00210100_least_bittern.gdb"
			FilePrefix = "E00210100_leabit"
		elif (CodeBird =="LEFL"):
			OutGDB ="E01458800_least_flycatcher.gdb"
			FilePrefix = "E01458800_leafly"
		elif (CodeBird =="LEGO"):
			OutGDB ="E03103200_lesser_goldfinch.gdb"
			FilePrefix = "E03103200_lesgol"
		elif (CodeBird =="LEGR"):
			OutGDB ="E00159600_least_grebe.gdb"
			FilePrefix = "E00159600_leagre"
		elif (CodeBird =="LENI"):
			OutGDB ="E00776700_lesser_nighthawk.gdb"
			FilePrefix = "E00776700_lesnig"
		elif (CodeBird =="LEOW"):
			OutGDB ="E00755500_long_eared_owl.gdb"
			FilePrefix = "E00755500_loeowl"
		elif (CodeBird =="LEPC"):
			OutGDB ="E00155200_lesser_prairie_chicken.gdb"
			FilePrefix = "E00155200_lepchi"
		elif (CodeBird =="LESA"):
			OutGDB ="E00407600_least_sandpiper.gdb"
			FilePrefix = "E00407600_leasan"
		elif (CodeBird =="LESC"):
			OutGDB ="E00051100_lesser_scaup.gdb"
			FilePrefix = "E00051100_lessca"
		elif (CodeBird =="LETE"):
			OutGDB ="E00444000_least_tern.gdb"
			FilePrefix = "E00444000_leater1"
		elif (CodeBird =="LEWO"):
			OutGDB ="E01087000_lewiss_woodpecker.gdb"
			FilePrefix = "E01087000_lewwoo"
		elif (CodeBird =="LEYE"):
			OutGDB ="E00397700_lesser_yellowlegs.gdb"
			FilePrefix = "E00397700_lesyel"
		elif (CodeBird =="LIGU"):
			OutGDB ="E00429100_little_gull.gdb"
			FilePrefix = "E00429100_litgul"
		elif (CodeBird =="LIMP"):
			OutGDB ="E00369200_limpkin.gdb"
			FilePrefix = "E00369200_limpki"
		elif (CodeBird =="LISP"):
			OutGDB ="E02990400_lincolns_sparrow.gdb"
			FilePrefix = "E02990400_linspa"
		elif (CodeBird =="LOSH"):
			OutGDB ="E01767200_loggerhead_shrike.gdb"
			FilePrefix = "E01767200_logshr"
		elif (CodeBird =="LOWA"):
			OutGDB ="E02777300_louisiana_waterthrush.gdb"
			FilePrefix = "E02777300_louwat"
		elif (CodeBird =="LTDU"):
			OutGDB ="E00054000_long_tailed_duck.gdb"
			FilePrefix = "E00054000_lotduc"
		elif (CodeBird =="LTJA"):
			OutGDB ="E00426212_long_tailed_jaeger.gdb"
			FilePrefix = "E00426212_lotjae"
		elif (CodeBird =="LUWA"):
			OutGDB ="E02780000_lucys_warbler.gdb"
			FilePrefix = "E02780000_lucwar"
		elif (CodeBird =="MACU"):
			OutGDB ="E00690900_mangrove_cuckoo.gdb"
			FilePrefix = "E00690900_mancuc"
		elif (CodeBird =="MAFR"):
			OutGDB ="E00194176_magnificent_frigatebird.gdb"
			FilePrefix = "E00194176_magfri"
		elif (CodeBird =="MAGO"):
			OutGDB ="E00401900_marbled_godwit.gdb"
			FilePrefix = "E00401900_margod"
		elif (CodeBird =="MAHU"):
			OutGDB ="E00881400_magnificent_hummingbird.gdb"
			FilePrefix = "E00881400_maghum"
		elif (CodeBird =="MALL"):
			OutGDB ="E00039600_mallard.gdb"
			FilePrefix = "E00039600_mallar"
		elif (CodeBird =="MAMU"):
			OutGDB ="E00426254_marbled_murrelet.gdb"
			FilePrefix = "E00426254_marmur"
		elif (CodeBird =="MAWA"):
			OutGDB ="E02788200_magnolia_warbler.gdb"
			FilePrefix = "E02788200_magwar"
		elif (CodeBird =="MAWR"):
			OutGDB ="E02127600_marsh_wren.gdb"
			FilePrefix = "E02127600_marwre"
		elif (CodeBird =="MCLO"):
			OutGDB ="E02776600_mccowns_longspur.gdb"
			FilePrefix = "E02776600_mcclon"
		elif (CodeBird =="MECH"):
			OutGDB ="E02026800_mexican_chickadee.gdb"
			FilePrefix = "E02026800_mexchi"
		elif (CodeBird =="MEDU"):
			OutGDB ="E00040000_mallard_mexican.gdb"
			FilePrefix = "E00040000_mexduc"
		elif (CodeBird =="MEGU"):
			OutGDB ="E00431400_mew_gull.gdb"
			FilePrefix = "E00431400_mewgul"
		elif (CodeBird =="MEJA"):
			OutGDB ="E01885800_mexican_jay.gdb"
			FilePrefix = "E01885800_mexjay4"
		elif (CodeBird =="MERL"):
			OutGDB ="E01158215_merlin.gdb"
			FilePrefix = "E01158215_merlin"
		elif (CodeBird =="MGWA"):
			OutGDB ="E02782200_macgillivrays_warbler.gdb"
			FilePrefix = "E02782200_macwar"
		elif (CodeBird =="MIKI"):
			OutGDB ="E00263400_mississippi_kite.gdb"
			FilePrefix = "E00263400_miskit"
		elif (CodeBird =="MKBU"):
			OutGDB ="E02776800_mckays_bunting.gdb"
			FilePrefix = "E02776800_mckbun"
		elif (CodeBird =="MOBL"):
			OutGDB ="E02449900_mountain_bluebird.gdb"
			FilePrefix = "E02449900_moublu"
		elif (CodeBird =="MOCH"):
			OutGDB ="E02025800_mountain_chickadee.gdb"
			FilePrefix = "E02025800_mouchi"
		elif (CodeBird =="MODO"):
			OutGDB ="E00501500_mourning_dove.gdb"
			FilePrefix = "E00501500_moudov"
		elif (CodeBird =="MODU"):
			OutGDB ="E00040900_mottled_duck.gdb"
			FilePrefix = "E00040900_motduc"
		elif (CodeBird =="MONQ"):
			OutGDB ="E00091300_montezuma_quail.gdb"
			FilePrefix = "E00091300_monqua"
		elif (CodeBird =="MOPA"):
			OutGDB ="E01158936_monk_parakeet.gdb"
			FilePrefix = "E01158936_monpar"
		elif (CodeBird =="MOPL"):
			OutGDB ="E00392450_mountain_plover.gdb"
			FilePrefix = "E00392450_mouplo"
		elif (CodeBird =="MOUQ"):
			OutGDB ="E00076800_mountain_quail.gdb"
			FilePrefix = "E00076800_mouqua"
		elif (CodeBird =="MOWA"):
			OutGDB ="E02782400_mourning_warbler.gdb"
			FilePrefix = "E02782400_mouwar"
		elif (CodeBird =="MUDU"):
			OutGDB ="E00034700_muscovy_duck.gdb"
			FilePrefix = "E00034700_musduc"
		elif (CodeBird =="MUSW"):
			OutGDB ="E00029600_mute_swan.gdb"
			FilePrefix = "E00029600_mutswa"
		elif (CodeBird =="NAWA"):
			OutGDB ="E02780100_nashville_warbler.gdb"
			FilePrefix = "E02780100_naswar"
		elif (CodeBird =="NECO"):
			OutGDB ="E00198500_neotropic_cormorant.gdb"
			FilePrefix = "E00198500_neocor"
		elif (CodeBird =="NHOW"):
			OutGDB ="E00733400_northern_hawk_owl.gdb"
			FilePrefix = "E00733400_nohowl"
		elif (CodeBird =="NOBO"):
			OutGDB ="E00080500_northern_bobwhite.gdb"
			FilePrefix = "E00080500_norbob"
		elif (CodeBird =="NOBT"):
			OutGDB ="E01380400_northern_beardless_tyrannulet.gdb"
			FilePrefix = "E01380400_nobtyr"
		elif (CodeBird =="NOCA"):
			OutGDB ="E03023300_northern_cardinal.gdb"
			FilePrefix = "E03023300_norcar"
		elif (CodeBird =="NOCR"):
			OutGDB ="E01907800_northwestern_crow.gdb"
			FilePrefix = "E01907800_norcro"
		elif (CodeBird =="NOFL"):
			OutGDB ="E01130800_northern_flicker.gdb"
			FilePrefix = "E01130800_norfli"
		elif (CodeBird =="NOFU"):
			OutGDB ="E00171600_northern_fulmar.gdb"
			FilePrefix = "E00171600_norful"
		elif (CodeBird =="NOGA"):
			OutGDB ="E00196400_northern_gannet.gdb"
			FilePrefix = "E00196400_norgan"
		elif (CodeBird =="NOGO"):
			OutGDB ="E00282720_northern_goshawk.gdb"
			FilePrefix = "E00282720_norgos"
		elif (CodeBird =="NOHA"):
			OutGDB ="E00265500_northern_harrier.gdb"
			FilePrefix = "E00265500_norhar"
		elif (CodeBird =="NOMO"):
			OutGDB ="E02646400_northern_mockingbird.gdb"
			FilePrefix = "E02646400_normoc"
		elif (CodeBird =="NOPA"):
			OutGDB ="E02786500_northern_parula.gdb"
			FilePrefix = "E02786500_norpar"
		elif (CodeBird =="NOPI"):
			OutGDB ="E00044600_northern_pintail.gdb"
			FilePrefix = "E00044600_norpin"
		elif (CodeBird =="NOPO"):
			OutGDB ="E00734900_northern_pygmy_owl.gdb"
			FilePrefix = "E00734900_nopowl"
		elif (CodeBird =="NOWA"):
			OutGDB ="E02777400_northern_waterthrush.gdb"
			FilePrefix = "E02777400_norwat"
		elif (CodeBird =="NRWS"):
			OutGDB ="E01994000_northern_rough_winged_swallow.gdb"
			FilePrefix = "E01994000_nrwswa"
		elif (CodeBird =="NSHO"):
			OutGDB ="E00043900_northern_shoveler.gdb"
			FilePrefix = "E00043900_norsho"
		elif (CodeBird =="NSHR"):
			OutGDB ="E01768400_northern_shrike.gdb"
			FilePrefix = "E01768400_norshr"
		elif (CodeBird =="NSWO"):
			OutGDB ="E00760200_northern_saw_whet_owl.gdb"
			FilePrefix = "E00760200_nswowl"
		elif (CodeBird =="NUWO"):
			OutGDB ="E01114700_nuttalls_woodpecker.gdb"
			FilePrefix = "E01114700_nutwoo"
		elif (CodeBird =="OATI"):
			OutGDB ="E02047500_oak_titmouse.gdb"
			FilePrefix = "E02047500_oaktit"
		elif (CodeBird =="OCWA"):
			OutGDB ="E02779300_orange_crowned_warbler.gdb"
			FilePrefix = "E02779300_orcwar"
		elif (CodeBird =="OLSP"):
			OutGDB ="E02953700_olive_sparrow.gdb"
			FilePrefix = "E02953700_olispa"
		elif (CodeBird =="OLWA"):
			OutGDB ="E02776300_olive_warbler.gdb"
			FilePrefix = "E02776300_oliwar"
		elif (CodeBird =="OROR"):
			OutGDB ="E03054600_orchard_oriole.gdb"
			FilePrefix = "E03054600_orcori"
		elif (CodeBird =="OSFL"):
			OutGDB ="E01451600_olive_sided_flycatcher.gdb"
			FilePrefix = "E01451600_olsfly"
		elif (CodeBird =="OSPR"):
			OutGDB ="E00237600_osprey.gdb"
			FilePrefix = "E00237600_osprey"
		elif (CodeBird =="OVEN"):
			OutGDB ="E02776900_ovenbird.gdb"
			FilePrefix = "E02776900_ovenbi1"
		elif (CodeBird =="PABU"):
			OutGDB ="E03033300_painted_bunting.gdb"
			FilePrefix = "E03033300_paibun"
		elif (CodeBird =="PAGP"):
			OutGDB ="E00380560_pacific_golden_plover.gdb"
			FilePrefix = "E00380560_pagplo"
		elif (CodeBird =="PAJA"):
			OutGDB ="E00426210_parasitic_jaeger.gdb"
			FilePrefix = "E00426210_parjae"
		elif (CodeBird =="PALO"):
			OutGDB ="E00156500_pacific_loon.gdb"
			FilePrefix = "E00156500_pacloo"
		elif (CodeBird =="PARE"):
			OutGDB ="E02810100_painted_redstart.gdb"
			FilePrefix = "E02810100_paired"
		elif (CodeBird =="PAWA"):
			OutGDB ="E02792900_palm_warbler.gdb"
			FilePrefix = "E02792900_palwar"
		elif (CodeBird =="PBGR"):
			OutGDB ="E00160100_pied_billed_grebe.gdb"
			FilePrefix = "E00160100_pibgre"
		elif (CodeBird =="PECO"):
			OutGDB ="E00201000_pelagic_cormorant.gdb"
			FilePrefix = "E00201000_pelcor"
		elif (CodeBird =="PEFA"):
			OutGDB ="E01158261_peregrine_falcon.gdb"
			FilePrefix = "E01158261_perfal"
		elif (CodeBird =="PHAI"):
			OutGDB ="E02775500_phainopepla.gdb"
			FilePrefix = "E02775500_phaino"
		elif (CodeBird =="PHVI"):
			OutGDB ="E01784900_philadelphia_vireo.gdb"
			FilePrefix = "E01784900_phivir"
		elif (CodeBird =="PIGR"):
			OutGDB ="E03084900_pine_grosbeak.gdb"
			FilePrefix = "E03084900_pingro"
		elif (CodeBird =="PIGU"):
			OutGDB ="E00426244_pigeon_guillemot.gdb"
			FilePrefix = "E00426244_piggui"
		elif (CodeBird =="PIJA"):
			OutGDB ="E01881550_pinyon_jay.gdb"
			FilePrefix = "E01881550_pinjay"
		elif (CodeBird =="PIPL"):
			OutGDB ="E00390100_piping_plover.gdb"
			FilePrefix = "E00390100_pipplo"
		elif (CodeBird =="PISI"):
			OutGDB ="E03102100_pine_siskin.gdb"
			FilePrefix = "E03102100_pinsis"
		elif (CodeBird =="PIWA"):
			OutGDB ="E02793300_pine_warbler.gdb"
			FilePrefix = "E02793300_pinwar"
		elif (CodeBird =="PIWO"):
			OutGDB ="E01139600_pileated_woodpecker.gdb"
			FilePrefix = "E01139600_pilwoo"
		elif (CodeBird =="PLCH"):
			OutGDB ="E00062600_plain_chachalaca.gdb"
			FilePrefix = "E00062600_placha"
		elif (CodeBird =="POJA"):
			OutGDB ="E00426209_pomarine_jaeger.gdb"
			FilePrefix = "E00426209_pomjae"
		elif (CodeBird =="PRAW"):
			OutGDB ="E02795600_prairie_warbler.gdb"
			FilePrefix = "E02795600_prawar"
		elif (CodeBird =="PRFA"):
			OutGDB ="E01158283_prairie_falcon.gdb"
			FilePrefix = "E01158283_prafal"
		elif (CodeBird =="PROW"):
			OutGDB ="E02778300_prothonotary_warbler.gdb"
			FilePrefix = "E02778300_prowar"
		elif (CodeBird =="PSFL"):
			OutGDB ="E01460000_pacific_slope_flycatcher.gdb"
			FilePrefix = "E01460000_pasfly"
		elif (CodeBird =="PUFI"):
			OutGDB ="E03087840_purple_finch.gdb"
			FilePrefix = "E03087840_purfin"
		elif (CodeBird =="PUMA"):
			OutGDB ="E01995300_purple_martin.gdb"
			FilePrefix = "E01995300_purmar"
		elif (CodeBird =="PUSA"):
			OutGDB ="E00407200_purple_sandpiper.gdb"
			FilePrefix = "E00407200_pursan"
		elif (CodeBird =="PYNU"):
			OutGDB ="E02077300_pygmy_nuthatch.gdb"
			FilePrefix = "E02077300_pygnut"
		elif (CodeBird =="PYRR"):
			OutGDB ="E03025300_pyrrhuloxia.gdb"
			FilePrefix = "E03025300_pyrrhu"
		elif (CodeBird =="RAZO"):
			OutGDB ="E00426233_razorbill.gdb"
			FilePrefix = "E00426233_razorb"
		elif (CodeBird =="RBGR"):
			OutGDB ="E03027300_rose_breasted_grosbeak.gdb"
			FilePrefix = "E03027300_robgro"
		elif (CodeBird =="RBGU"):
			OutGDB ="E00431900_ring_billed_gull.gdb"
			FilePrefix = "E00431900_ribgul"
		elif (CodeBird =="RBME"):
			OutGDB ="E00056100_red_breasted_merganser.gdb"
			FilePrefix = "E00056100_rebmer"
		elif (CodeBird =="RBNU"):
			OutGDB ="E02075700_red_breasted_nuthatch.gdb"
			FilePrefix = "E02075700_rebnut"
		elif (CodeBird =="RBPI"):
			OutGDB ="E00476900_red_billed_pigeon.gdb"
			FilePrefix = "E00476900_rebpig1"
		elif (CodeBird =="RBSA"):
			OutGDB ="E01094100_red_breasted_sapsucker.gdb"
			FilePrefix = "E01094100_rebsap"
		elif (CodeBird =="RBWO"):
			OutGDB ="E01092500_red_bellied_woodpecker.gdb"
			FilePrefix = "E01092500_rebwoo"
		elif (CodeBird =="RCKI"):
			OutGDB ="E02193900_ruby_crowned_kinglet.gdb"
			FilePrefix = "E02193900_ruckin"
		elif (CodeBird =="RCPA"):
			OutGDB ="E01159180_red_crowned_parrot.gdb"
			FilePrefix = "E01159180_recpar"
		elif (CodeBird =="RCSP"):
			OutGDB ="E02961600_rufous_crowned_sparrow.gdb"
			FilePrefix = "E02961600_rucspa"
		elif (CodeBird =="RCWO"):
			OutGDB ="E01118400_red_cockaded_woodpecker.gdb"
			FilePrefix = "E01118400_recwoo"
		elif (CodeBird =="RECR"):
			OutGDB ="E03097300_red_crossbill.gdb"
			FilePrefix = "E03097300_redcro"
		elif (CodeBird =="REDH"):
			OutGDB ="E00049700_redhead.gdb"
			FilePrefix = "E00049700_redhea"
		elif (CodeBird =="REEG"):
			OutGDB ="E00217700_reddish_egret.gdb"
			FilePrefix = "E00217700_redegr"
		elif (CodeBird =="REKN"):
			OutGDB ="E00402900_red_knot.gdb"
			FilePrefix = "E00402900_redkno"
		elif (CodeBird =="REPH"):
			OutGDB ="E00413800_red_phalarope.gdb"
			FilePrefix = "E00413800_redpha1"
		elif (CodeBird =="REVI"):
			OutGDB ="E01785000_red_eyed_vireo.gdb"
			FilePrefix = "E01785000_reevir"
		elif (CodeBird =="RFCO"):
			OutGDB ="E00200900_red_faced_cormorant.gdb"
			FilePrefix = "E00200900_refcor"
		elif (CodeBird =="RFWA"):
			OutGDB ="E02809500_red_faced_warbler.gdb"
			FilePrefix = "E02809500_refwar"
		elif (CodeBird =="RHAU"):
			OutGDB ="E00426273_rhinoceros_auklet.gdb"
			FilePrefix = "E00426273_rhiauk"
		elif (CodeBird =="RHWO"):
			OutGDB ="E01087300_red_headed_woodpecker.gdb"
			FilePrefix = "E01087300_rehwoo"
		elif (CodeBird =="RIKI"):
			OutGDB ="E00992800_ringed_kingfisher.gdb"
			FilePrefix = "E00992800_rinkin1"
		elif (CodeBird =="RLHA"):
			OutGDB ="E00300700_rough_legged_hawk.gdb"
			FilePrefix = "E00300700_rolhaw"
		elif (CodeBird =="RNDU"):
			OutGDB ="E00049900_ring_necked_duck.gdb"
			FilePrefix = "E00049900_rinduc"
		elif (CodeBird =="RNEP"):
			OutGDB ="E00133800_ring_necked_pheasant.gdb"
			FilePrefix = "E00133800_rinphe"
		elif (CodeBird =="RNGR"):
			OutGDB ="E00161400_red_necked_grebe.gdb"
			FilePrefix = "E00161400_rengre"
		elif (CodeBird =="RNPH"):
			OutGDB ="E00413700_red_necked_phalarope.gdb"
			FilePrefix = "E00413700_renpha"
		elif (CodeBird =="RNSA"):
			OutGDB ="E01093800_red_naped_sapsucker.gdb"
			FilePrefix = "E01093800_rensap"
		elif (CodeBird =="ROGO"):
			OutGDB ="E00025900_rosss_goose.gdb"
			FilePrefix = "E00025900_rosgoo"
		elif (CodeBird =="ROPI"):
			OutGDB ="E00467300_rock_pigeon.gdb"
			FilePrefix = "E00467300_rocpig"
		elif (CodeBird =="ROPT"):
			OutGDB ="E00149000_rock_ptarmigan.gdb"
			FilePrefix = "E00149000_rocpta1"
		elif (CodeBird =="ROSA"):
			OutGDB ="E00407100_rock_sandpiper.gdb"
			FilePrefix = "E00407100_rocsan"
		elif (CodeBird =="ROSP"):
			OutGDB ="E00232400_roseate_spoonbill.gdb"
			FilePrefix = "E00232400_rosspo1"
		elif (CodeBird =="ROWR"):
			OutGDB ="E02088410_rock_wren.gdb"
			FilePrefix = "E02088410_rocwre"
		elif (CodeBird =="ROYT"):
			OutGDB ="E00451500_royal_tern.gdb"
			FilePrefix = "E00451500_royter1"
		elif (CodeBird =="RSHA"):
			OutGDB ="E00295900_red_shouldered_hawk.gdb"
			FilePrefix = "E00295900_reshaw"
		elif (CodeBird =="RTHA"):
			OutGDB ="E00298900_red_tailed_hawk.gdb"
			FilePrefix = "E00298900_rethaw"
		elif (CodeBird =="RTHU"):
			OutGDB ="E00889600_ruby_throated_hummingbird.gdb"
			FilePrefix = "E00889600_rthhum"
		elif (CodeBird =="RTLO"):
			OutGDB ="E00156100_red_throated_loon.gdb"
			FilePrefix = "E00156100_retloo"
		elif (CodeBird =="RUBL"):
			OutGDB ="E03041600_rusty_blackbird.gdb"
			FilePrefix = "E03041600_rusbla"
		elif (CodeBird =="RUDU"):
			OutGDB ="E00056700_ruddy_duck.gdb"
			FilePrefix = "E00056700_rudduc"
		elif (CodeBird =="RUGD"):
			OutGDB ="E00504900_ruddy_ground_dove.gdb"
			FilePrefix = "E00504900_rugdov"
		elif (CodeBird =="RUGR"):
			OutGDB ="E00144300_ruffed_grouse.gdb"
			FilePrefix = "E00144300_rufgro"
		elif (CodeBird =="RUHU"):
			OutGDB ="E00892400_rufous_hummingbird.gdb"
			FilePrefix = "E00892400_rufhum"
		elif (CodeBird =="RUTU"):
			OutGDB ="E00402300_ruddy_turnstone.gdb"
			FilePrefix = "E00402300_rudtur"
		elif (CodeBird =="RWBL"):
			OutGDB ="E03033900_red_winged_blackbird.gdb"
			FilePrefix = "E03033900_rewbla"
		elif (CodeBird =="RWSP"):
			OutGDB ="E02964400_rufous_winged_sparrow.gdb"
			FilePrefix = "E02964400_ruwspa"
		elif (CodeBird =="SACR"):
			OutGDB ="E00371700_sandhill_crane.gdb"
			FilePrefix = "E00371700_sancra"
		elif (CodeBird =="SAGS"):
			OutGDB ="E02975400_bells_sparrow.gdb"
			FilePrefix = "E02975400_belspa2"
		elif (CodeBird =="SAND"):
			OutGDB ="E00405900_sanderling.gdb"
			FilePrefix = "E00405900_sander"
		elif (CodeBird =="SAPH"):
			OutGDB ="E01463300_says_phoebe.gdb"
			FilePrefix = "E01463300_saypho"
		elif (CodeBird =="SATE"):
			OutGDB ="E00452500_sandwich_tern.gdb"
			FilePrefix = "E00452500_santer1"
		elif (CodeBird =="SATH"):
			OutGDB ="E02642300_sage_thrasher.gdb"
			FilePrefix = "E02642300_sagthr"
		elif (CodeBird =="SAVS"):
			OutGDB ="E02976200_savannah_sparrow.gdb"
			FilePrefix = "E02976200_savspa"
		elif (CodeBird =="SBAN"):
			OutGDB ="E00695000_smooth_billed_ani.gdb"
			FilePrefix = "E00695000_smbani"
		elif (CodeBird =="SBDO"):
			OutGDB ="E00408000_short_billed_dowitcher.gdb"
			FilePrefix = "E00408000_shbdow"
		elif (CodeBird =="SBFL"):
			OutGDB ="E01502400_sulphur_bellied_flycatcher.gdb"
			FilePrefix = "E01502400_subfly"
		elif (CodeBird =="SBOR"):
			OutGDB ="E03061400_spot_breasted_oriole.gdb"
			FilePrefix = "E03061400_spbori"
		elif (CodeBird =="SCOR"):
			OutGDB ="E03063600_scotts_oriole.gdb"
			FilePrefix = "E03063600_scoori"
		elif (CodeBird =="SCQU"):
			OutGDB ="E00077500_scaled_quail.gdb"
			FilePrefix = "E00077500_scaqua"
		elif (CodeBird =="SCTA"):
			OutGDB ="E03016300_scarlet_tanager.gdb"
			FilePrefix = "E03016300_scatan"
		elif (CodeBird =="SEOW"):
			OutGDB ="E00757100_short_eared_owl.gdb"
			FilePrefix = "E00757100_sheowl"
		elif (CodeBird =="SEPL"):
			OutGDB ="E00389900_semipalmated_plover.gdb"
			FilePrefix = "E00389900_semplo"
		elif (CodeBird =="SESA"):
			OutGDB ="E00407805_semipalmated_sandpiper.gdb"
			FilePrefix = "E00407805_semsan"
		elif (CodeBird =="SESP"):
			OutGDB ="E02982600_seaside_sparrow.gdb"
			FilePrefix = "E02982600_seaspa"
		elif (CodeBird =="SEWR"):
			OutGDB ="E02124800_sedge_wren.gdb"
			FilePrefix = "E02124800_sedwre"
		elif (CodeBird =="SKLA"):
			OutGDB ="E01984100_sky_lark.gdb"
			FilePrefix = "E01984100_skylar"
		elif (CodeBird =="SMLO"):
			OutGDB ="E02776500_smiths_longspur.gdb"
			FilePrefix = "E02776500_smilon"
		elif (CodeBird =="SNBU"):
			OutGDB ="E02776640_snow_bunting.gdb"
			FilePrefix = "E02776640_snobun"
		elif (CodeBird =="SNEG"):
			OutGDB ="E00216900_snowy_egret.gdb"
			FilePrefix = "E00216900_snoegr"
		elif (CodeBird =="SNGO"):
			OutGDB ="E00025400_snow_goose.gdb"
			FilePrefix = "E00025400_snogoo"
		elif (CodeBird =="SNKI"):
			OutGDB ="E00262500_snail_kite.gdb"
			FilePrefix = "E00262500_snakit"
		elif (CodeBird =="SNOW"):
			OutGDB ="E00731400_snowy_owl.gdb"
			FilePrefix = "E00731400_snoowl1"
		elif (CodeBird =="SNPL"):
			OutGDB ="E00388700_snowy_plover.gdb"
			FilePrefix = "E00388700_snoplo5"
		elif (CodeBird =="SORA"):
			OutGDB ="E00349500_sora.gdb"
			FilePrefix = "E00349500_sora"
		elif (CodeBird =="SOSA"):
			OutGDB ="E00396400_solitary_sandpiper.gdb"
			FilePrefix = "E00396400_solsan"
		elif (CodeBird =="SOSP"):
			OutGDB ="E02986400_song_sparrow.gdb"
			FilePrefix = "E02986400_sonspa"
		elif (CodeBird =="SOVI"):
			OutGDB ="E01780500_solitary_vireo_sp.gdb"
			FilePrefix = "E01780500_solvir1"
		elif (CodeBird =="SPDO"):
			OutGDB ="E00486000_spotted_dove.gdb"
			FilePrefix = "E00486000_spodov"
		elif (CodeBird =="SPGR"):
			OutGDB ="E00146100_spruce_grouse.gdb"
			FilePrefix = "E00146100_sprgro"
		elif (CodeBird =="SPOW"):
			OutGDB ="E00752100_spotted_owl.gdb"
			FilePrefix = "E00752100_spoowl"
		elif (CodeBird =="SPPI"):
			OutGDB ="E02767500_spragues_pipit.gdb"
			FilePrefix = "E02767500_sprpip"
		elif (CodeBird =="SPSA"):
			OutGDB ="E00396200_spotted_sandpiper.gdb"
			FilePrefix = "E00396200_sposan"
		elif (CodeBird =="SPTO"):
			OutGDB ="E02958000_spotted_towhee.gdb"
			FilePrefix = "E02958000_spotow"
		elif (CodeBird =="SSHA"):
			OutGDB ="E00280700_sharp_shinned_hawk.gdb"
			FilePrefix = "E00280700_shshaw"
		elif (CodeBird =="STEI"):
			OutGDB ="E00051400_stellers_eider.gdb"
			FilePrefix = "E00051400_steeid"
		elif (CodeBird =="STFL"):
			OutGDB ="E01506800_scissor_tailed_flycatcher.gdb"
			FilePrefix = "E01506800_sctfly"
		elif (CodeBird =="STGR"):
			OutGDB ="E00154100_sharp_tailed_grouse.gdb"
			FilePrefix = "E00154100_shtgro"
		elif (CodeBird =="STHA"):
			OutGDB ="E00298000_short_tailed_hawk.gdb"
			FilePrefix = "E00298000_shthaw"
		elif (CodeBird =="STJA"):
			OutGDB ="E01881600_stellers_jay.gdb"
			FilePrefix = "E01881600_stejay"
		elif (CodeBird =="STKI"):
			OutGDB ="E00243100_swallow_tailed_kite.gdb"
			FilePrefix = "E00243100_swtkit"
		elif (CodeBird =="STSA"):
			OutGDB ="E00405300_stilt_sandpiper.gdb"
			FilePrefix = "E00405300_stisan"
		elif (CodeBird =="STSP"):
			OutGDB ="E02982500_nelsons_saltmarsh_sparrow_sharp_tailed_sparrow.gdb"
			FilePrefix = "E02982500_shtspa"
		elif (CodeBird =="SURF"):
			OutGDB ="E00403520_surfbird.gdb"
			FilePrefix = "E00403520_surfbi"
		elif (CodeBird =="SUSC"):
			OutGDB ="E00053000_surf_scoter.gdb"
			FilePrefix = "E00053000_sursco"
		elif (CodeBird =="SUTA"):
			OutGDB ="E03016000_summer_tanager.gdb"
			FilePrefix = "E03016000_sumtan"
		elif (CodeBird =="SWHA"):
			OutGDB ="E00298400_swainsons_hawk.gdb"
			FilePrefix = "E00298400_swahaw"
		elif (CodeBird =="SWSP"):
			OutGDB ="E02990800_swamp_sparrow.gdb"
			FilePrefix = "E02990800_swaspa"
		elif (CodeBird =="SWTH"):
			OutGDB ="E02460200_swainsons_thrush.gdb"
			FilePrefix = "E02460200_swathr"
		elif (CodeBird =="SWWA"):
			OutGDB ="E02778400_swainsons_warbler.gdb"
			FilePrefix = "E02778400_swawar"
		elif (CodeBird =="TBKI"):
			OutGDB ="E01504800_thick_billed_kingbird.gdb"
			FilePrefix = "E01504800_thbkin"
		elif (CodeBird =="TBMU"):
			OutGDB ="E00426227_thick_billed_murre.gdb"
			FilePrefix = "E00426227_thbmur"
		elif (CodeBird =="TEWA"):
			OutGDB ="E02779200_tennessee_warbler.gdb"
			FilePrefix = "E02779200_tenwar"
		elif (CodeBird =="THGU"):
			OutGDB ="E00434900_thayers_gull.gdb"
			FilePrefix = "E00434900_thagul"
		elif (CodeBird =="TOSO"):
			OutGDB ="E02450100_townsends_solitaire.gdb"
			FilePrefix = "E02450100_towsol"
		elif (CodeBird =="TOWA"):
			OutGDB ="E02797100_townsends_warbler.gdb"
			FilePrefix = "E02797100_towwar"
		elif (CodeBird =="TRBL"):
			OutGDB ="E03036900_tricolored_blackbird.gdb"
			FilePrefix = "E03036900_tribla"
		elif (CodeBird =="TRES"):
			OutGDB ="E01997200_tree_swallow.gdb"
			FilePrefix = "E01997200_treswa"
		elif (CodeBird =="TRHE"):
			OutGDB ="E00217400_tricolored_heron.gdb"
			FilePrefix = "E00217400_triher"
		elif (CodeBird =="TRKI"):
			OutGDB ="E01503800_tropical_kingbird.gdb"
			FilePrefix = "E01503800_trokin"
		elif (CodeBird =="TRPA"):
			OutGDB ="E02786800_tropical_parula.gdb"
			FilePrefix = "E02786800_tropar"
		elif (CodeBird =="TRUS"):
			OutGDB ="E00029900_trumpeter_swan.gdb"
			FilePrefix = "E00029900_truswa"
		elif (CodeBird =="TUSW"):
			OutGDB ="E00030200_tundra_swan.gdb"
			FilePrefix = "E00030200_tunswa"
		elif (CodeBird =="TUTI"):
			OutGDB ="E02048400_tufted_titmouse.gdb"
			FilePrefix = "E02048400_tuftit"
		elif (CodeBird =="TUVU"):
			OutGDB ="E00236200_turkey_vulture.gdb"
			FilePrefix = "E00236200_turvul"
		elif (CodeBird =="UPSA"):
			OutGDB ="E00399100_upland_sandpiper.gdb"
			FilePrefix = "E00399100_uplsan"
		elif (CodeBird =="VABU"):
			OutGDB ="E03032800_varied_bunting.gdb"
			FilePrefix = "E03032800_varbun"
		elif (CodeBird =="VASW"):
			OutGDB ="E00809700_vauxs_swift.gdb"
			FilePrefix = "E00809700_vauswi"
		elif (CodeBird =="VATH"):
			OutGDB ="E02493300_varied_thrush.gdb"
			FilePrefix = "E02493300_varthr"
		elif (CodeBird =="VCHU"):
			OutGDB ="E00919400_violet_crowned_hummingbird.gdb"
			FilePrefix = "E00919400_vichum"
		elif (CodeBird =="VEER"):
			OutGDB ="E02459200_veery.gdb"
			FilePrefix = "E02459200_veery"
		elif (CodeBird =="VEFL"):
			OutGDB ="E01463700_vermilion_flycatcher.gdb"
			FilePrefix = "E01463700_verfly"
		elif (CodeBird =="VERD"):
			OutGDB ="E02050100_verdin.gdb"
			FilePrefix = "E02050100_verdin"
		elif (CodeBird =="VESP"):
			OutGDB ="E02973600_vesper_sparrow.gdb"
			FilePrefix = "E02973600_vesspa"
		elif (CodeBird =="VGSW"):
			OutGDB ="E01998100_violet_green_swallow.gdb"
			FilePrefix = "E01998100_vigswa"
		elif (CodeBird =="VIRA"):
			OutGDB ="E00340100_virginia_rail.gdb"
			FilePrefix = "E00340100_virrai"
		elif (CodeBird =="VIWA"):
			OutGDB ="E02780400_virginias_warbler.gdb"
			FilePrefix = "E02780400_virwar"
		elif (CodeBird =="WATA"):
			OutGDB ="E00396800_wandering_tattler.gdb"
			FilePrefix = "E00396800_wantat1"
		elif (CodeBird =="WAVI"):
			OutGDB ="E01782800_warbling_vireo.gdb"
			FilePrefix = "E01782800_warvir"
		elif (CodeBird =="WBNU"):
			OutGDB ="E02076100_white_breasted_nuthatch.gdb"
			FilePrefix = "E02076100_whbnut"
		elif (CodeBird =="WCPI"):
			OutGDB ="E00476800_white_crowned_pigeon.gdb"
			FilePrefix = "E00476800_whcpig2"
		elif (CodeBird =="WCSP"):
			OutGDB ="E02994600_white_crowned_sparrow.gdb"
			FilePrefix = "E02994600_whcspa"
		elif (CodeBird =="WEBL"):
			OutGDB ="E02449100_western_bluebird.gdb"
			FilePrefix = "E02449100_wesblu"
		elif (CodeBird =="WEGR"):
			OutGDB ="E00163300_western_grebe.gdb"
			FilePrefix = "E00163300_wesgre"
		elif (CodeBird =="WEGU"):
			OutGDB ="E00432000_western_gull.gdb"
			FilePrefix = "E00432000_wesgul"
		elif (CodeBird =="WEKI"):
			OutGDB ="E01505100_western_kingbird.gdb"
			FilePrefix = "E01505100_weskin"
		elif (CodeBird =="WEME"):
			OutGDB ="E03040600_western_meadowlark.gdb"
			FilePrefix = "E03040600_wesmea"
		elif (CodeBird =="WESA"):
			OutGDB ="E00407806_western_sandpiper.gdb"
			FilePrefix = "E00407806_wessan"
		elif (CodeBird =="WESJ"):
			OutGDB ="E01883900_western_scrub_jay.gdb"
			FilePrefix = "E01883900_wesjay"
		elif (CodeBird =="WESO"):
			OutGDB ="E00715000_western_screech_owl.gdb"
			FilePrefix = "E00715000_wesowl1"
		elif (CodeBird =="WETA"):
			OutGDB ="E03016400_western_tanager.gdb"
			FilePrefix = "E03016400_westan"
		elif (CodeBird =="WEVI"):
			OutGDB ="E01775000_white_eyed_vireo.gdb"
			FilePrefix = "E01775000_whevir"
		elif (CodeBird =="WEWA"):
			OutGDB ="E02777200_worm_eating_warbler.gdb"
			FilePrefix = "E02777200_woewar1"
		elif (CodeBird =="WEWP"):
			OutGDB ="E01452900_western_wood_pewee.gdb"
			FilePrefix = "E01452900_wewpew"
		elif (CodeBird =="WFIB"):
			OutGDB ="E00227000_white_faced_ibis.gdb"
			FilePrefix = "E00227000_whfibi"
		elif (CodeBird =="WHCR"):
			OutGDB ="E00373200_whooping_crane.gdb"
			FilePrefix = "E00373200_whocra"
		elif (CodeBird =="WHIB"):
			OutGDB ="E00226500_white_ibis.gdb"
			FilePrefix = "E00226500_whiibi"
		elif (CodeBird =="WHIM"):
			OutGDB ="E00399400_whimbrel.gdb"
			FilePrefix = "E00399400_whimbr"
		elif (CodeBird =="WHSO"):
			OutGDB ="E00717300_whiskered_screech_owl.gdb"
			FilePrefix = "E00717300_whsowl1"
		elif (CodeBird =="WHWO"):
			OutGDB ="E01118500_white_headed_woodpecker.gdb"
			FilePrefix = "E01118500_whhwoo"
		elif (CodeBird =="WIFL"):
			OutGDB ="E01457600_willow_flycatcher.gdb"
			FilePrefix = "E01457600_wilfly"
		elif (CodeBird =="WILL"):
			OutGDB ="E00397400_willet.gdb"
			FilePrefix = "E00397400_willet1"
		elif (CodeBird =="WIPH"):
			OutGDB ="E00413600_wilsons_phalarope.gdb"
			FilePrefix = "E00413600_wilpha"
		elif (CodeBird =="WIPL"):
			OutGDB ="E00389200_wilsons_plover.gdb"
			FilePrefix = "E00389200_wilplo"
		elif (CodeBird =="WIPT"):
			OutGDB ="E00146900_willow_ptarmigan.gdb"
			FilePrefix = "E00146900_wilpta"
		elif (CodeBird =="WISA"):
			OutGDB ="E01093300_williamsons_sapsucker.gdb"
			FilePrefix = "E01093300_wilsap"
		elif (CodeBird =="WISN"):
			OutGDB ="E00410300_wilsons_snipe.gdb"
			FilePrefix = "E00410300_wilsni1"
		elif (CodeBird =="WITU"):
			OutGDB ="E00155300_wild_turkey.gdb"
			FilePrefix = "E00155300_wiltur"
		elif (CodeBird =="WIWA"):
			OutGDB ="E02809100_wilsons_warbler.gdb"
			FilePrefix = "E02809100_wlswar"
		elif (CodeBird =="WIWR"):
			OutGDB ="E02124710_pacific_winter_wren.gdb"
			FilePrefix = "E02124710_winwre"
		elif (CodeBird =="WODU"):
			OutGDB ="E00035700_wood_duck.gdb"
			FilePrefix = "E00035700_wooduc"
		elif (CodeBird =="WOST"):
			OutGDB ="E00194156_wood_stork.gdb"
			FilePrefix = "E00194156_woosto"
		elif (CodeBird =="WOTH"):
			OutGDB ="E02462200_wood_thrush.gdb"
			FilePrefix = "E02462200_woothr"
		elif (CodeBird =="WREN"):
			OutGDB ="E02330800_wrentit.gdb"
			FilePrefix = "E02330800_wrenti"
		elif (CodeBird =="WTDO"):
			OutGDB ="E00508300_white_tipped_dove.gdb"
			FilePrefix = "E00508300_whtdov"
		elif (CodeBird =="WTHA"):
			OutGDB ="E00293900_white_tailed_hawk.gdb"
			FilePrefix = "E00293900_whthaw"
		elif (CodeBird =="WTKI"):
			OutGDB ="E00239100_white_tailed_kite.gdb"
			FilePrefix = "E00239100_whtkit"
		elif (CodeBird =="WTPT"):
			OutGDB ="E00152200_white_tailed_ptarmigan.gdb"
			FilePrefix = "E00152200_whtpta1"
		elif (CodeBird =="WTSP"):
			OutGDB ="E02994100_white_throated_sparrow.gdb"
			FilePrefix = "E02994100_whtspa"
		elif (CodeBird =="WTSW"):
			OutGDB ="E00834500_white_throated_swift.gdb"
			FilePrefix = "E00834500_whtswi"
		elif (CodeBird =="WWCR"):
			OutGDB ="E03100500_white_winged_crossbill.gdb"
			FilePrefix = "E03100500_whwcro"
		elif (CodeBird =="WWDO"):
			OutGDB ="E00499200_white_winged_dove.gdb"
			FilePrefix = "E00499200_whwdov"
		elif (CodeBird =="WWSC"):
			OutGDB ="E00053100_white_winged_scoter.gdb"
			FilePrefix = "E00053100_whwsco"
		elif (CodeBird =="YBCH"):
			OutGDB ="E02813800_yellow_breasted_chat.gdb"
			FilePrefix = "E02813800_yebcha"
		elif (CodeBird =="YBCU"):
			OutGDB ="E00690700_yellow_billed_cuckoo.gdb"
			FilePrefix = "E00690700_yebcuc"
		elif (CodeBird =="YBFL"):
			OutGDB ="E01457300_yellow_bellied_flycatcher.gdb"
			FilePrefix = "E01457300_yebfly"
		elif (CodeBird =="YBLO"):
			OutGDB ="E00156800_yellow_billed_loon.gdb"
			FilePrefix = "E00156800_yebloo"
		elif (CodeBird =="YBMA"):
			OutGDB ="E01900100_yellow_billed_magpie.gdb"
			FilePrefix = "E01900100_yebmag"
		elif (CodeBird =="YBSA"):
			OutGDB ="E01093600_yellow_bellied_sapsucker.gdb"
			FilePrefix = "E01093600_yebsap"
		elif (CodeBird =="YCNH"):
			OutGDB ="E00224400_yellow_crowned_night_heron.gdb"
			FilePrefix = "E00224400_ycnher"
		elif (CodeBird =="YEJU"):
			OutGDB ="E02997800_yellow_eyed_junco.gdb"
			FilePrefix = "E02997800_yeejun"
		elif (CodeBird =="YERA"):
			OutGDB ="E00325700_yellow_rail.gdb"
			FilePrefix = "E00325700_yelrai"
		elif (CodeBird =="YEWA"):
			OutGDB ="E02788500_yellow_warbler.gdb"
			FilePrefix = "E02788500_yelwar"
		elif (CodeBird =="YFGU"):
			OutGDB ="E00432400_yellow_footed_gull.gdb"
			FilePrefix = "E00432400_yefgul"
		elif (CodeBird =="YHBL"):
			OutGDB ="E03041000_yellow_headed_blackbird.gdb"
			FilePrefix = "E03041000_yehbla"
		elif (CodeBird =="YRWA"):
			OutGDB ="E02793800_yellow_rumped_warbler.gdb"
			FilePrefix = "E02793800_yerwar"
		elif (CodeBird =="YTVI"):
			OutGDB ="E01778800_yellow_throated_vireo.gdb"
			FilePrefix = "E01778800_yetvir"
		elif (CodeBird =="YTWA"):
			OutGDB ="E02794600_yellow_throated_warbler.gdb"
			FilePrefix = "E02794600_yetwar"
		elif (CodeBird =="ZTHA"):
			OutGDB ="E00298600_zone_tailed_hawk.gdb"
			FilePrefix = "E00298600_zothaw"
		else: print InRaster + " not checked." #if for some reason the BBL code is not found it prints that the raster was not verified
		
		#verification process
		if arcpy.Exists("J:\\" + OutGDB + "\\" + FilePrefix + "_" +InRaster[0:-4]):
			pass #if the raster exists, nothing happens
		else: print InRaster + " does not exist." #if the raster does not exist it prints that

	A +=1 #this variable iterates to the next folder

print "Done" #Script completed
