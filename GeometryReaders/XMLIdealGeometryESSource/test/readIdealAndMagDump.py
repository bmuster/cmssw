import FWCore.ParameterSet.Config as cms

process = cms.Process("DBGeometryTest")
process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")
process.load("MagneticField.Engine.volumeBasedMagneticField_090322_2pi_scaled_cfi")

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(1)
        )

process.source = cms.Source("EmptySource")

process.myprint = cms.OutputModule("AsciiOutputModule")

#Produces two output files dumpGeoHistory and dumpSpecsGeoHistory
process.prod = cms.EDAnalyzer("PerfectGeometryAnalyzer"
                              ,ddRootNodeName = cms.string("cms:OCMS")
                              ,dumpPosInfo = cms.untracked.bool(True)
                              ,dumpSpecs = cms.untracked.bool(True)
                              ,dumpGeoHistory = cms.untracked.bool(True)
                              ,label = cms.untracked.string("") #actually defaults to blank and IS default Geometry.
                              ,isMagField = cms.untracked.bool(False) 
                              ,outFileName = cms.untracked.string("GeoHistory") #GeoHistory is the default name
                              ,numNodesToDump = cms.untracked.uint32(0) #0 means ALL, you can limit the number of nodes dumped.
                              )

#Produces two output files dumpMagF and dumpSpecsMagF
process.prodmag = cms.EDAnalyzer("PerfectGeometryAnalyzer"
                              ,ddRootNodeName = cms.string("cmsMagneticField:MAGF")
                              ,dumpPosInfo = cms.untracked.bool(True)
                              ,dumpSpecs = cms.untracked.bool(True)
                              ,dumpGeoHistory = cms.untracked.bool(True)
                              ,label = cms.untracked.string("magfield") #actually defaults to blank and IS default Geometry.
                              ,isMagField = cms.untracked.bool(True) 
                              ,outFileName = cms.untracked.string("MagF") #GeoHistory is the default name
                              ,numNodesToDump = cms.untracked.uint32(0) #0 means ALL, you can limit the number of nodes dumped.
                              )

process.Timing = cms.Service("Timing")

process.p1 = cms.Path(process.prodmag*process.prod)
process.e1 = cms.EndPath(process.myprint)
