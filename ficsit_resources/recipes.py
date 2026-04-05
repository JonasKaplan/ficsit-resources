from ficsit_resources.types import Item, Recipe, Rate
from ficsit_resources.items import Items

class Recipes:
    IronPlate = Recipe(
        "Iron Plate",
        [(Items.IronIngot, Rate(30.0))],
        [(Items.IronPlate, Rate(20.0))],
    )
    IronRod = Recipe(
        "Iron Rod",
        [(Items.IronIngot, Rate(15.0))],
        [(Items.IronRod, Rate(15.0))],
    )
    IronAlloyIngot = Recipe(
        "Alternate: Iron Alloy Ingot",
        [(Items.IronOre, Rate(40.0)), (Items.CopperOre, Rate(10.0))],
        [(Items.IronIngot, Rate(75.0))],
    )
    NitroRocketFuel = Recipe(
        "Alternate: Nitro Rocket Fuel",
        [(Items.Fuel, Rate(100.0)), (Items.NitrogenGas, Rate(75.0)), (Items.Sulfur, Rate(100.0)), (Items.Coal, Rate(50.0))],
        [(Items.RocketFuel, Rate(150.0)), (Items.CompactedCoal, Rate(25.0))],
    )
    RocketFuel = Recipe(
        "Rocket Fuel",
        [(Items.Turbofuel, Rate(60.0)), (Items.NitricAcid, Rate(10.0))],
        [(Items.RocketFuel, Rate(100.0)), (Items.CompactedCoal, Rate(10.0))],
    )
    PackagedRocketFuel = Recipe(
        "Packaged Rocket Fuel",
        [(Items.RocketFuel, Rate(120.0)), (Items.EmptyFluidTank, Rate(60.0))],
        [(Items.PackagedRocketFuel, Rate(60.0))],
    )
    UnpackageRocketFuel = Recipe(
        "Unpackage Rocket Fuel",
        [(Items.PackagedRocketFuel, Rate(60.0))],
        [(Items.RocketFuel, Rate(120.0)), (Items.EmptyFluidTank, Rate(60.0))],
    )
    DarkIonFuel = Recipe(
        "Alternate: Dark-Ion Fuel",
        [(Items.PackagedRocketFuel, Rate(240.0)), (Items.DarkMatterCrystal, Rate(80.0))],
        [(Items.IonizedFuel, Rate(200.0)), (Items.CompactedCoal, Rate(40.0))],
    )
    DarkMatterResidue = Recipe(
        "Dark Matter Residue",
        [(Items.ReanimatedSAM, Rate(50.0))],
        [(Items.DarkMatterResidue, Rate(100.0))],
    )
    ExcitedPhotonicMatter = Recipe(
        "Excited Photonic Matter",
        [],
        [(Items.ExcitedPhotonicMatter, Rate(200.0))],
    )
    DarkMatterCrystal = Recipe(
        "Dark Matter Crystal",
        [(Items.Diamonds, Rate(30.0)), (Items.DarkMatterResidue, Rate(150.0))],
        [(Items.DarkMatterCrystal, Rate(30.0))],
    )
    SuperpositionOscillator = Recipe(
        "Superposition Oscillator",
        [(Items.DarkMatterCrystal, Rate(30.0)), (Items.CrystalOscillator, Rate(5.0)), (Items.AlcladAluminumSheet, Rate(45.0)), (Items.ExcitedPhotonicMatter, Rate(125.0))],
        [(Items.SuperpositionOscillator, Rate(5.0)), (Items.DarkMatterResidue, Rate(125.0))],
    )
    NeuralQuantumProcessor = Recipe(
        "Neural-Quantum Processor",
        [(Items.TimeCrystal, Rate(15.0)), (Items.Supercomputer, Rate(3.0)), (Items.FicsiteTrigon, Rate(45.0)), (Items.ExcitedPhotonicMatter, Rate(75.0))],
        [(Items.NeuralQuantumProcessor, Rate(3.0)), (Items.DarkMatterResidue, Rate(75.0))],
    )
    AIExpansionServer = Recipe(
        "AI Expansion Server",
        [(Items.MagneticFieldGenerator, Rate(4.0)), (Items.NeuralQuantumProcessor, Rate(4.0)), (Items.SuperpositionOscillator, Rate(4.0)), (Items.ExcitedPhotonicMatter, Rate(100.0))],
        [(Items.AIExpansionServer, Rate(4.0)), (Items.DarkMatterResidue, Rate(100.0))],
    )
    IonizedFuel = Recipe(
        "Ionized Fuel",
        [(Items.RocketFuel, Rate(40.0)), (Items.PowerShard, Rate(2.5))],
        [(Items.IonizedFuel, Rate(40.0)), (Items.CompactedCoal, Rate(5.0))],
    )
    PackagedIonizedFuel = Recipe(
        "Packaged Ionized Fuel",
        [(Items.IonizedFuel, Rate(80.0)), (Items.EmptyFluidTank, Rate(40.0))],
        [(Items.PackagedIonizedFuel, Rate(40.0))],
    )
    UnpackageIonizedFuel = Recipe(
        "Unpackage Ionized Fuel",
        [(Items.PackagedIonizedFuel, Rate(40.0))],
        [(Items.IonizedFuel, Rate(80.0)), (Items.EmptyFluidTank, Rate(40.0))],
    )
    TurboDiamonds = Recipe(
        "Alternate: Turbo Diamonds",
        [(Items.Coal, Rate(600.0)), (Items.PackagedTurbofuel, Rate(40.0))],
        [(Items.Diamonds, Rate(60.0))],
    )
    SAMFluctuator = Recipe(
        "SAM Fluctuator",
        [(Items.ReanimatedSAM, Rate(60.0)), (Items.Wire, Rate(50.0)), (Items.SteelPipe, Rate(30.0))],
        [(Items.SAMFluctuator, Rate(10.0))],
    )
    FicsiteTrigon = Recipe(
        "Ficsite Trigon",
        [(Items.FicsiteIngot, Rate(10.0))],
        [(Items.FicsiteTrigon, Rate(30.0))],
    )
    FicsiteIngotIron = Recipe(
        "Ficsite Ingot (Iron)",
        [(Items.ReanimatedSAM, Rate(40.0)), (Items.IronIngot, Rate(240.0))],
        [(Items.FicsiteIngot, Rate(10.0))],
    )
    TimeCrystal = Recipe(
        "Time Crystal",
        [(Items.Diamonds, Rate(12.0))],
        [(Items.TimeCrystal, Rate(6.0))],
    )
    Diamonds = Recipe(
        "Diamonds",
        [(Items.Coal, Rate(600.0))],
        [(Items.Diamonds, Rate(30.0))],
    )
    ReanimatedSAM = Recipe(
        "Reanimated SAM",
        [(Items.SAM, Rate(120.0))],
        [(Items.ReanimatedSAM, Rate(30.0))],
    )
    BiochemicalSculptor = Recipe(
        "Biochemical Sculptor",
        [(Items.AssemblyDirectorSystem, Rate(0.5)), (Items.FicsiteTrigon, Rate(40.0)), (Items.Water, Rate(10.0))],
        [(Items.BiochemicalSculptor, Rate(2.0))],
    )
    FicsiteIngotAluminum = Recipe(
        "Ficsite Ingot (Aluminum)",
        [(Items.ReanimatedSAM, Rate(60.0)), (Items.AluminumIngot, Rate(120.0))],
        [(Items.FicsiteIngot, Rate(30.0))],
    )
    FicsiteIngotCaterium = Recipe(
        "Ficsite Ingot (Caterium)",
        [(Items.ReanimatedSAM, Rate(45.0)), (Items.CateriumIngot, Rate(60.0))],
        [(Items.FicsiteIngot, Rate(15.0))],
    )
    BauxiteCaterium = Recipe(
        "Bauxite (Caterium)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.CateriumOre, Rate(150.0))],
        [(Items.Bauxite, Rate(120.0))],
    )
    BauxiteCopper = Recipe(
        "Bauxite (Copper)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.CopperOre, Rate(180.0))],
        [(Items.Bauxite, Rate(120.0))],
    )
    CateriumOreCopper = Recipe(
        "Caterium Ore (Copper)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.CopperOre, Rate(150.0))],
        [(Items.CateriumOre, Rate(120.0))],
    )
    CateriumOreQuartz = Recipe(
        "Caterium Ore (Quartz)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.RawQuartz, Rate(120.0))],
        [(Items.CateriumOre, Rate(120.0))],
    )
    CoalIron = Recipe(
        "Coal (Iron)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.IronOre, Rate(180.0))],
        [(Items.Coal, Rate(120.0))],
    )
    CoalLimestone = Recipe(
        "Coal (Limestone)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.Limestone, Rate(360.0))],
        [(Items.Coal, Rate(120.0))],
    )
    CopperOreQuartz = Recipe(
        "Copper Ore (Quartz)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.RawQuartz, Rate(100.0))],
        [(Items.CopperOre, Rate(120.0))],
    )
    CopperOreSulfur = Recipe(
        "Copper Ore (Sulfur)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.Sulfur, Rate(120.0))],
        [(Items.CopperOre, Rate(120.0))],
    )
    IronOreLimestone = Recipe(
        "Iron Ore (Limestone)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.Limestone, Rate(240.0))],
        [(Items.IronOre, Rate(120.0))],
    )
    LimestoneSulfur = Recipe(
        "Limestone (Sulfur)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.Sulfur, Rate(20.0))],
        [(Items.Limestone, Rate(120.0))],
    )
    NitrogenGasBauxite = Recipe(
        "Nitrogen Gas (Bauxite)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.Bauxite, Rate(100.0))],
        [(Items.NitrogenGas, Rate(120.0))],
    )
    NitrogenGasCaterium = Recipe(
        "Nitrogen Gas (Caterium)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.CateriumOre, Rate(120.0))],
        [(Items.NitrogenGas, Rate(120.0))],
    )
    RawQuartzBauxite = Recipe(
        "Raw Quartz (Bauxite)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.Bauxite, Rate(100.0))],
        [(Items.RawQuartz, Rate(120.0))],
    )
    RawQuartzCoal = Recipe(
        "Raw Quartz (Coal)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.Coal, Rate(240.0))],
        [(Items.RawQuartz, Rate(120.0))],
    )
    SulfurCoal = Recipe(
        "Sulfur (Coal)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.Coal, Rate(200.0))],
        [(Items.Sulfur, Rate(120.0))],
    )
    SulfurIron = Recipe(
        "Sulfur (Iron)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.IronOre, Rate(300.0))],
        [(Items.Sulfur, Rate(120.0))],
    )
    UraniumOreBauxite = Recipe(
        "Uranium Ore (Bauxite)",
        [(Items.ReanimatedSAM, Rate(10.0)), (Items.Bauxite, Rate(480.0))],
        [(Items.Uranium, Rate(120.0))],
    )
    Turbofuel = Recipe(
        "Turbofuel",
        [(Items.Fuel, Rate(22.5)), (Items.CompactedCoal, Rate(15.0))],
        [(Items.Turbofuel, Rate(18.75))],
    )
    PackagedTurbofuel = Recipe(
        "Packaged Turbofuel",
        [(Items.Turbofuel, Rate(20.0)), (Items.EmptyCanister, Rate(20.0))],
        [(Items.PackagedTurbofuel, Rate(20.0))],
    )
    UnpackageTurbofuel = Recipe(
        "Unpackage Turbofuel",
        [(Items.PackagedTurbofuel, Rate(20.0))],
        [(Items.Turbofuel, Rate(20.0)), (Items.EmptyCanister, Rate(20.0))],
    )
    Charcoal = Recipe(
        "Alternate: Charcoal",
        [(Items.Wood, Rate(15.0))],
        [(Items.Coal, Rate(150.0))],
    )
    Biocoal = Recipe(
        "Alternate: Biocoal",
        [(Items.Biomass, Rate(37.5))],
        [(Items.Coal, Rate(45.0))],
    )
    CompactedCoal = Recipe(
        "Alternate: Compacted Coal",
        [(Items.Coal, Rate(25.0)), (Items.Sulfur, Rate(25.0))],
        [(Items.CompactedCoal, Rate(25.0))],
    )
    CircuitBoard = Recipe(
        "Circuit Board",
        [(Items.CopperSheet, Rate(15.0)), (Items.Plastic, Rate(30.0))],
        [(Items.CircuitBoard, Rate(7.5))],
    )
    Fuel = Recipe(
        "Fuel",
        [(Items.CrudeOil, Rate(60.0))],
        [(Items.Fuel, Rate(40.0)), (Items.PolymerResin, Rate(30.0))],
    )
    PetroleumCoke = Recipe(
        "Petroleum Coke",
        [(Items.HeavyOilResidue, Rate(40.0))],
        [(Items.PetroleumCoke, Rate(120.0))],
    )
    Plastic = Recipe(
        "Plastic",
        [(Items.CrudeOil, Rate(30.0))],
        [(Items.Plastic, Rate(20.0)), (Items.HeavyOilResidue, Rate(10.0))],
    )
    Rubber = Recipe(
        "Rubber",
        [(Items.CrudeOil, Rate(30.0))],
        [(Items.Rubber, Rate(20.0)), (Items.HeavyOilResidue, Rate(20.0))],
    )
    ResidualFuel = Recipe(
        "Residual Fuel",
        [(Items.HeavyOilResidue, Rate(60.0))],
        [(Items.Fuel, Rate(40.0))],
    )
    ResidualPlastic = Recipe(
        "Residual Plastic",
        [(Items.PolymerResin, Rate(60.0)), (Items.Water, Rate(20.0))],
        [(Items.Plastic, Rate(20.0))],
    )
    ResidualRubber = Recipe(
        "Residual Rubber",
        [(Items.PolymerResin, Rate(40.0)), (Items.Water, Rate(40.0))],
        [(Items.Rubber, Rate(20.0))],
    )
    PinkDiamonds = Recipe(
        "Alternate: Pink Diamonds",
        [(Items.Coal, Rate(120.0)), (Items.QuartzCrystal, Rate(45.0))],
        [(Items.Diamonds, Rate(15.0))],
    )
    PetroleumDiamonds = Recipe(
        "Alternate: Petroleum Diamonds",
        [(Items.PetroleumCoke, Rate(720.0))],
        [(Items.Diamonds, Rate(30.0))],
    )
    OilBasedDiamonds = Recipe(
        "Alternate: Oil-Based Diamonds",
        [(Items.CrudeOil, Rate(200.0))],
        [(Items.Diamonds, Rate(40.0))],
    )
    CloudyDiamonds = Recipe(
        "Alternate: Cloudy Diamonds",
        [(Items.Coal, Rate(240.0)), (Items.Limestone, Rate(480.0))],
        [(Items.Diamonds, Rate(20.0))],
    )
    DarkMatterTrap = Recipe(
        "Alternate: Dark Matter Trap",
        [(Items.TimeCrystal, Rate(30.0)), (Items.DarkMatterResidue, Rate(150.0))],
        [(Items.DarkMatterCrystal, Rate(60.0))],
    )
    DarkMatterCrystallization = Recipe(
        "Alternate: Dark Matter Crystallization",
        [(Items.DarkMatterResidue, Rate(200.0))],
        [(Items.DarkMatterCrystal, Rate(20.0))],
    )
    WetConcrete = Recipe(
        "Alternate: Wet Concrete",
        [(Items.Limestone, Rate(120.0)), (Items.Water, Rate(100.0))],
        [(Items.Concrete, Rate(80.0))],
    )
    TurboHeavyFuel = Recipe(
        "Alternate: Turbo Heavy Fuel",
        [(Items.HeavyOilResidue, Rate(37.5)), (Items.CompactedCoal, Rate(30.0))],
        [(Items.Turbofuel, Rate(30.0))],
    )
    SteelRod = Recipe(
        "Alternate: Steel Rod",
        [(Items.SteelIngot, Rate(12.0))],
        [(Items.IronRod, Rate(48.0))],
    )
    SteelBeam = Recipe(
        "Steel Beam",
        [(Items.SteelIngot, Rate(60.0))],
        [(Items.SteelBeam, Rate(15.0))],
    )
    SteelPipe = Recipe(
        "Steel Pipe",
        [(Items.SteelIngot, Rate(30.0))],
        [(Items.SteelPipe, Rate(20.0))],
    )
    SteelIngot = Recipe(
        "Steel Ingot",
        [(Items.IronOre, Rate(45.0)), (Items.Coal, Rate(45.0))],
        [(Items.SteelIngot, Rate(45.0))],
    )
    VersatileFramework = Recipe(
        "Versatile Framework",
        [(Items.ModularFrame, Rate(2.5)), (Items.SteelBeam, Rate(30.0))],
        [(Items.VersatileFramework, Rate(5.0))],
    )
    SteelCanister = Recipe(
        "Alternate: Steel Canister",
        [(Items.SteelIngot, Rate(40.0))],
        [(Items.EmptyCanister, Rate(40.0))],
    )
    EmptyCanister = Recipe(
        "Empty Canister",
        [(Items.Plastic, Rate(30.0))],
        [(Items.EmptyCanister, Rate(60.0))],
    )
    PackagedFuel = Recipe(
        "Packaged Fuel",
        [(Items.Fuel, Rate(40.0)), (Items.EmptyCanister, Rate(40.0))],
        [(Items.PackagedFuel, Rate(40.0))],
    )
    LiquidBiofuel = Recipe(
        "Liquid Biofuel",
        [(Items.SolidBiofuel, Rate(90.0)), (Items.Water, Rate(45.0))],
        [(Items.LiquidBiofuel, Rate(60.0))],
    )
    PackagedLiquidBiofuel = Recipe(
        "Packaged Liquid Biofuel",
        [(Items.LiquidBiofuel, Rate(40.0)), (Items.EmptyCanister, Rate(40.0))],
        [(Items.PackagedLiquidBiofuel, Rate(40.0))],
    )
    PackagedOil = Recipe(
        "Packaged Oil",
        [(Items.CrudeOil, Rate(30.0)), (Items.EmptyCanister, Rate(30.0))],
        [(Items.PackagedOil, Rate(30.0))],
    )
    PackagedHeavyOilResidue = Recipe(
        "Packaged Heavy Oil Residue",
        [(Items.HeavyOilResidue, Rate(30.0)), (Items.EmptyCanister, Rate(30.0))],
        [(Items.PackagedHeavyOilResidue, Rate(30.0))],
    )
    PackagedWater = Recipe(
        "Packaged Water",
        [(Items.Water, Rate(60.0)), (Items.EmptyCanister, Rate(60.0))],
        [(Items.PackagedWater, Rate(60.0))],
    )
    UnpackageLiquidBiofuel = Recipe(
        "Unpackage Liquid Biofuel",
        [(Items.PackagedLiquidBiofuel, Rate(60.0))],
        [(Items.LiquidBiofuel, Rate(60.0)), (Items.EmptyCanister, Rate(60.0))],
    )
    UnpackageFuel = Recipe(
        "Unpackage Fuel",
        [(Items.PackagedFuel, Rate(60.0))],
        [(Items.Fuel, Rate(60.0)), (Items.EmptyCanister, Rate(60.0))],
    )
    UnpackageOil = Recipe(
        "Unpackage Oil",
        [(Items.PackagedOil, Rate(60.0))],
        [(Items.CrudeOil, Rate(60.0)), (Items.EmptyCanister, Rate(60.0))],
    )
    UnpackageHeavyOilResidue = Recipe(
        "Unpackage Heavy Oil Residue",
        [(Items.PackagedHeavyOilResidue, Rate(20.0))],
        [(Items.HeavyOilResidue, Rate(20.0)), (Items.EmptyCanister, Rate(20.0))],
    )
    UnpackageWater = Recipe(
        "Unpackage Water",
        [(Items.PackagedWater, Rate(120.0))],
        [(Items.Water, Rate(120.0)), (Items.EmptyCanister, Rate(120.0))],
    )
    SteamedCopperSheet = Recipe(
        "Alternate: Steamed Copper Sheet",
        [(Items.CopperIngot, Rate(22.5)), (Items.Water, Rate(22.5))],
        [(Items.CopperSheet, Rate(22.5))],
    )
    RubberConcrete = Recipe(
        "Alternate: Rubber Concrete",
        [(Items.Limestone, Rate(100.0)), (Items.Rubber, Rate(20.0))],
        [(Items.Concrete, Rate(90.0))],
    )
    RecycledRubber = Recipe(
        "Alternate: Recycled Rubber",
        [(Items.Plastic, Rate(30.0)), (Items.Fuel, Rate(30.0))],
        [(Items.Rubber, Rate(60.0))],
    )
    PureQuartzCrystal = Recipe(
        "Alternate: Pure Quartz Crystal",
        [(Items.RawQuartz, Rate(67.5)), (Items.Water, Rate(37.5))],
        [(Items.QuartzCrystal, Rate(52.5))],
    )
    QuartzCrystal = Recipe(
        "Quartz Crystal",
        [(Items.RawQuartz, Rate(37.5))],
        [(Items.QuartzCrystal, Rate(22.5))],
    )
    PureIronIngot = Recipe(
        "Alternate: Pure Iron Ingot",
        [(Items.IronOre, Rate(35.0)), (Items.Water, Rate(20.0))],
        [(Items.IronIngot, Rate(65.0))],
    )
    PureCopperIngot = Recipe(
        "Alternate: Pure Copper Ingot",
        [(Items.CopperOre, Rate(15.0)), (Items.Water, Rate(10.0))],
        [(Items.CopperIngot, Rate(37.5))],
    )
    PureCateriumIngot = Recipe(
        "Alternate: Pure Caterium Ingot",
        [(Items.CateriumOre, Rate(24.0)), (Items.Water, Rate(24.0))],
        [(Items.CateriumIngot, Rate(12.0))],
    )
    PureAluminumIngot = Recipe(
        "Alternate: Pure Aluminum Ingot",
        [(Items.AluminumScrap, Rate(60.0))],
        [(Items.AluminumIngot, Rate(30.0))],
    )
    AluminumCasing = Recipe(
        "Aluminum Casing",
        [(Items.AluminumIngot, Rate(90.0))],
        [(Items.AluminumCasing, Rate(60.0))],
    )
    AlcladAluminumSheet = Recipe(
        "Alclad Aluminum Sheet",
        [(Items.AluminumIngot, Rate(30.0)), (Items.CopperIngot, Rate(10.0))],
        [(Items.AlcladAluminumSheet, Rate(30.0))],
    )
    AluminaSolution = Recipe(
        "Alumina Solution",
        [(Items.Bauxite, Rate(120.0)), (Items.Water, Rate(180.0))],
        [(Items.AluminaSolution, Rate(120.0)), (Items.Silica, Rate(50.0))],
    )
    AluminumScrap = Recipe(
        "Aluminum Scrap",
        [(Items.AluminaSolution, Rate(240.0)), (Items.Coal, Rate(120.0))],
        [(Items.AluminumScrap, Rate(360.0)), (Items.Water, Rate(120.0))],
    )
    PackagedAluminaSolution = Recipe(
        "Packaged Alumina Solution",
        [(Items.AluminaSolution, Rate(120.0)), (Items.EmptyCanister, Rate(120.0))],
        [(Items.PackagedAluminaSolution, Rate(120.0))],
    )
    AluminumIngot = Recipe(
        "Aluminum Ingot",
        [(Items.AluminumScrap, Rate(90.0)), (Items.Silica, Rate(75.0))],
        [(Items.AluminumIngot, Rate(60.0))],
    )
    CheapSilica = Recipe(
        "Alternate: Cheap Silica",
        [(Items.RawQuartz, Rate(22.5)), (Items.Limestone, Rate(37.5))],
        [(Items.Silica, Rate(52.5))],
    )
    InsulatedCrystalOscillator = Recipe(
        "Alternate: Insulated Crystal Oscillator",
        [(Items.QuartzCrystal, Rate(18.75)), (Items.Rubber, Rate(13.125)), (Items.AILimiter, Rate(1.875))],
        [(Items.CrystalOscillator, Rate(1.875))],
    )
    UnpackageAluminaSolution = Recipe(
        "Unpackage Alumina Solution",
        [(Items.PackagedAluminaSolution, Rate(120.0))],
        [(Items.AluminaSolution, Rate(120.0)), (Items.EmptyCanister, Rate(120.0))],
    )
    PolymerResin = Recipe(
        "Alternate: Polymer Resin",
        [(Items.CrudeOil, Rate(60.0))],
        [(Items.PolymerResin, Rate(130.0)), (Items.HeavyOilResidue, Rate(20.0))],
    )
    PlasticSmartPlating = Recipe(
        "Alternate: Plastic Smart Plating",
        [(Items.ReinforcedIronPlate, Rate(2.5)), (Items.Rotor, Rate(2.5)), (Items.Plastic, Rate(7.5))],
        [(Items.SmartPlating, Rate(5.0))],
    )
    AutomatedSpeedWiring = Recipe(
        "Alternate: Automated Speed Wiring",
        [(Items.Stator, Rate(3.75)), (Items.Wire, Rate(75.0)), (Items.HighSpeedConnector, Rate(1.875))],
        [(Items.AutomatedWiring, Rate(7.5))],
    )
    EncasedIndustrialPipe = Recipe(
        "Alternate: Encased Industrial Pipe",
        [(Items.SteelPipe, Rate(24.0)), (Items.Concrete, Rate(20.0))],
        [(Items.EncasedIndustrialBeam, Rate(4.0))],
    )
    Motor = Recipe(
        "Motor",
        [(Items.Rotor, Rate(10.0)), (Items.Stator, Rate(10.0))],
        [(Items.Motor, Rate(5.0))],
    )
    QuickwireStator = Recipe(
        "Alternate: Quickwire Stator",
        [(Items.SteelPipe, Rate(16.0)), (Items.Quickwire, Rate(60.0))],
        [(Items.Stator, Rate(8.0))],
    )
    AutomatedWiring = Recipe(
        "Automated Wiring",
        [(Items.Stator, Rate(2.5)), (Items.Cable, Rate(50.0))],
        [(Items.AutomatedWiring, Rate(2.5))],
    )
    AILimiter = Recipe(
        "AI Limiter",
        [(Items.CopperSheet, Rate(25.0)), (Items.Quickwire, Rate(100.0))],
        [(Items.AILimiter, Rate(5.0))],
    )
    HeavyOilResidue = Recipe(
        "Alternate: Heavy Oil Residue",
        [(Items.CrudeOil, Rate(30.0))],
        [(Items.HeavyOilResidue, Rate(40.0)), (Items.PolymerResin, Rate(20.0))],
    )
    HeavyFlexibleFrame = Recipe(
        "Alternate: Heavy Flexible Frame",
        [(Items.ModularFrame, Rate(18.75)), (Items.EncasedIndustrialBeam, Rate(11.25)), (Items.Rubber, Rate(75.0)), (Items.Screw, Rate(390.0))],
        [(Items.HeavyModularFrame, Rate(3.75))],
    )
    Computer = Recipe(
        "Computer",
        [(Items.CircuitBoard, Rate(10.0)), (Items.Cable, Rate(20.0)), (Items.Plastic, Rate(40.0))],
        [(Items.Computer, Rate(2.5))],
    )
    HeavyEncasedFrame = Recipe(
        "Alternate: Heavy Encased Frame",
        [(Items.ModularFrame, Rate(7.5)), (Items.EncasedIndustrialBeam, Rate(9.375)), (Items.SteelPipe, Rate(33.75)), (Items.Concrete, Rate(20.625))],
        [(Items.HeavyModularFrame, Rate(2.8125))],
    )
    ModularEngine = Recipe(
        "Modular Engine",
        [(Items.Motor, Rate(2.0)), (Items.Rubber, Rate(15.0)), (Items.SmartPlating, Rate(2.0))],
        [(Items.ModularEngine, Rate(1.0))],
    )
    AdaptiveControlUnit = Recipe(
        "Adaptive Control Unit",
        [(Items.AutomatedWiring, Rate(5.0)), (Items.CircuitBoard, Rate(5.0)), (Items.HeavyModularFrame, Rate(1.0)), (Items.Computer, Rate(2.0))],
        [(Items.AdaptiveControlUnit, Rate(1.0))],
    )
    FusedWire = Recipe(
        "Alternate: Fused Wire",
        [(Items.CopperIngot, Rate(12.0)), (Items.CateriumIngot, Rate(3.0))],
        [(Items.Wire, Rate(90.0))],
    )
    FlexibleFramework = Recipe(
        "Alternate: Flexible Framework",
        [(Items.ModularFrame, Rate(3.75)), (Items.SteelBeam, Rate(22.5)), (Items.Rubber, Rate(30.0))],
        [(Items.VersatileFramework, Rate(7.5))],
    )
    ElectrodeCircuitBoard = Recipe(
        "Alternate: Electrode Circuit Board",
        [(Items.Rubber, Rate(20.0)), (Items.PetroleumCoke, Rate(40.0))],
        [(Items.CircuitBoard, Rate(5.0))],
    )
    ElectrodeAluminumScrap = Recipe(
        "Alternate: Electrode Aluminum Scrap",
        [(Items.AluminaSolution, Rate(180.0)), (Items.PetroleumCoke, Rate(60.0))],
        [(Items.AluminumScrap, Rate(300.0)), (Items.Water, Rate(105.0))],
    )
    DilutedPackagedFuel = Recipe(
        "Alternate: Diluted Packaged Fuel",
        [(Items.HeavyOilResidue, Rate(30.0)), (Items.PackagedWater, Rate(60.0))],
        [(Items.PackagedFuel, Rate(60.0))],
    )
    CopperRotor = Recipe(
        "Alternate: Copper Rotor",
        [(Items.CopperSheet, Rate(22.5)), (Items.Screw, Rate(195.0))],
        [(Items.Rotor, Rate(11.25))],
    )
    SteeledFrame = Recipe(
        "Alternate: Steeled Frame",
        [(Items.ReinforcedIronPlate, Rate(2.0)), (Items.SteelPipe, Rate(10.0))],
        [(Items.ModularFrame, Rate(3.0))],
    )
    SteelRotor = Recipe(
        "Alternate: Steel Rotor",
        [(Items.SteelPipe, Rate(10.0)), (Items.Wire, Rate(30.0))],
        [(Items.Rotor, Rate(5.0))],
    )
    CopperSheet = Recipe(
        "Copper Sheet",
        [(Items.CopperIngot, Rate(20.0))],
        [(Items.CopperSheet, Rate(10.0))],
    )
    SmartPlating = Recipe(
        "Smart Plating",
        [(Items.ReinforcedIronPlate, Rate(2.0)), (Items.Rotor, Rate(2.0))],
        [(Items.SmartPlating, Rate(2.0))],
    )
    CopperAlloyIngot = Recipe(
        "Alternate: Copper Alloy Ingot",
        [(Items.CopperOre, Rate(50.0)), (Items.IronOre, Rate(50.0))],
        [(Items.CopperIngot, Rate(100.0))],
    )
    CokeSteelIngot = Recipe(
        "Alternate: Coke Steel Ingot",
        [(Items.IronOre, Rate(75.0)), (Items.PetroleumCoke, Rate(75.0))],
        [(Items.SteelIngot, Rate(100.0))],
    )
    CoatedIronPlate = Recipe(
        "Alternate: Coated Iron Plate",
        [(Items.IronIngot, Rate(37.5)), (Items.Plastic, Rate(7.5))],
        [(Items.IronPlate, Rate(75.0))],
    )
    CoatedIronCanister = Recipe(
        "Alternate: Coated Iron Canister",
        [(Items.IronPlate, Rate(30.0)), (Items.CopperSheet, Rate(15.0))],
        [(Items.EmptyCanister, Rate(60.0))],
    )
    CoatedCable = Recipe(
        "Alternate: Coated Cable",
        [(Items.Wire, Rate(37.5)), (Items.HeavyOilResidue, Rate(15.0))],
        [(Items.Cable, Rate(67.5))],
    )
    BoltedFrame = Recipe(
        "Alternate: Bolted Frame",
        [(Items.ReinforcedIronPlate, Rate(7.5)), (Items.Screw, Rate(140.0))],
        [(Items.ModularFrame, Rate(5.0))],
    )
    AdheredIronPlate = Recipe(
        "Alternate: Adhered Iron Plate",
        [(Items.IronPlate, Rate(11.25)), (Items.Rubber, Rate(3.75))],
        [(Items.ReinforcedIronPlate, Rate(3.75))],
    )
    TurboPressureMotor = Recipe(
        "Alternate: Turbo Pressure Motor",
        [(Items.Motor, Rate(7.5)), (Items.PressureConversionCube, Rate(1.875)), (Items.PackagedNitrogenGas, Rate(45.0)), (Items.Stator, Rate(15.0))],
        [(Items.TurboMotor, Rate(3.75))],
    )
    EncasedPlutoniumCell = Recipe(
        "Encased Plutonium Cell",
        [(Items.PlutoniumPellet, Rate(10.0)), (Items.Concrete, Rate(20.0))],
        [(Items.EncasedPlutoniumCell, Rate(5.0))],
    )
    PressureConversionCube = Recipe(
        "Pressure Conversion Cube",
        [(Items.FusedModularFrame, Rate(1.0)), (Items.RadioControlUnit, Rate(2.0))],
        [(Items.PressureConversionCube, Rate(1.0))],
    )
    NitricAcid = Recipe(
        "Nitric Acid",
        [(Items.NitrogenGas, Rate(120.0)), (Items.Water, Rate(30.0)), (Items.IronPlate, Rate(10.0))],
        [(Items.NitricAcid, Rate(30.0))],
    )
    NonFissileUranium = Recipe(
        "Non-Fissile Uranium",
        [(Items.UraniumWaste, Rate(37.5)), (Items.Silica, Rate(25.0)), (Items.NitricAcid, Rate(15.0)), (Items.SulfuricAcid, Rate(15.0))],
        [(Items.NonFissileUranium, Rate(50.0)), (Items.Water, Rate(15.0))],
    )
    CopperPowder = Recipe(
        "Copper Powder",
        [(Items.CopperIngot, Rate(300.0))],
        [(Items.CopperPowder, Rate(50.0))],
    )
    PlutoniumPellet = Recipe(
        "Plutonium Pellet",
        [(Items.NonFissileUranium, Rate(100.0)), (Items.UraniumWaste, Rate(25.0))],
        [(Items.PlutoniumPellet, Rate(30.0))],
    )
    PlutoniumFuelRod = Recipe(
        "Plutonium Fuel Rod",
        [(Items.EncasedPlutoniumCell, Rate(7.5)), (Items.SteelBeam, Rate(4.5)), (Items.ElectromagneticControlRod, Rate(1.5)), (Items.HeatSink, Rate(2.5))],
        [(Items.PlutoniumFuelRod, Rate(0.25))],
    )
    PackagedNitricAcid = Recipe(
        "Packaged Nitric Acid",
        [(Items.NitricAcid, Rate(30.0)), (Items.EmptyFluidTank, Rate(30.0))],
        [(Items.PackagedNitricAcid, Rate(30.0))],
    )
    NuclearPasta = Recipe(
        "Nuclear Pasta",
        [(Items.CopperPowder, Rate(100.0)), (Items.PressureConversionCube, Rate(0.5))],
        [(Items.NuclearPasta, Rate(0.5))],
    )
    UnpackageNitricAcid = Recipe(
        "Unpackage Nitric Acid",
        [(Items.PackagedNitricAcid, Rate(20.0))],
        [(Items.NitricAcid, Rate(20.0)), (Items.EmptyFluidTank, Rate(20.0))],
    )
    TurboBlendFuel = Recipe(
        "Alternate: Turbo Blend Fuel",
        [(Items.Fuel, Rate(15.0)), (Items.HeavyOilResidue, Rate(30.0)), (Items.Sulfur, Rate(22.5)), (Items.PetroleumCoke, Rate(22.5))],
        [(Items.Turbofuel, Rate(45.0))],
    )
    EncasedUraniumCell = Recipe(
        "Encased Uranium Cell",
        [(Items.Uranium, Rate(50.0)), (Items.Concrete, Rate(15.0)), (Items.SulfuricAcid, Rate(40.0))],
        [(Items.EncasedUraniumCell, Rate(25.0)), (Items.SulfuricAcid, Rate(10.0))],
    )
    CoolingSystem = Recipe(
        "Cooling System",
        [(Items.HeatSink, Rate(12.0)), (Items.Rubber, Rate(12.0)), (Items.Water, Rate(30.0)), (Items.NitrogenGas, Rate(150.0))],
        [(Items.CoolingSystem, Rate(6.0))],
    )
    Battery = Recipe(
        "Battery",
        [(Items.SulfuricAcid, Rate(50.0)), (Items.AluminaSolution, Rate(40.0)), (Items.AluminumCasing, Rate(20.0))],
        [(Items.Battery, Rate(20.0)), (Items.Water, Rate(30.0))],
    )
    Supercomputer = Recipe(
        "Supercomputer",
        [(Items.Computer, Rate(7.5)), (Items.AILimiter, Rate(3.75)), (Items.HighSpeedConnector, Rate(5.625)), (Items.Plastic, Rate(52.5))],
        [(Items.Supercomputer, Rate(1.875))],
    )
    RadioControlUnit = Recipe(
        "Radio Control Unit",
        [(Items.AluminumCasing, Rate(40.0)), (Items.CrystalOscillator, Rate(1.25)), (Items.Computer, Rate(2.5))],
        [(Items.RadioControlUnit, Rate(2.5))],
    )
    SulfuricAcid = Recipe(
        "Sulfuric Acid",
        [(Items.Sulfur, Rate(50.0)), (Items.Water, Rate(50.0))],
        [(Items.SulfuricAcid, Rate(50.0))],
    )
    PackagedSulfuricAcid = Recipe(
        "Packaged Sulfuric Acid",
        [(Items.SulfuricAcid, Rate(40.0)), (Items.EmptyCanister, Rate(40.0))],
        [(Items.PackagedSulfuricAcid, Rate(40.0))],
    )
    AssemblyDirectorSystem = Recipe(
        "Assembly Director System",
        [(Items.AdaptiveControlUnit, Rate(1.5)), (Items.Supercomputer, Rate(0.75))],
        [(Items.AssemblyDirectorSystem, Rate(0.75))],
    )
    SiliconHighSpeedConnector = Recipe(
        "Alternate: Silicon High-Speed Connector",
        [(Items.Quickwire, Rate(90.0)), (Items.Silica, Rate(37.5)), (Items.CircuitBoard, Rate(3.0))],
        [(Items.HighSpeedConnector, Rate(3.0))],
    )
    UnpackageSulfuricAcid = Recipe(
        "Unpackage Sulfuric Acid",
        [(Items.PackagedSulfuricAcid, Rate(60.0))],
        [(Items.SulfuricAcid, Rate(60.0)), (Items.EmptyCanister, Rate(60.0))],
    )
    SuperStateComputer = Recipe(
        "Alternate: Super-State Computer",
        [(Items.Computer, Rate(7.2)), (Items.ElectromagneticControlRod, Rate(2.4)), (Items.Battery, Rate(24.0)), (Items.Wire, Rate(60.0))],
        [(Items.Supercomputer, Rate(2.4))],
    )
    ElectromagneticControlRod = Recipe(
        "Electromagnetic Control Rod",
        [(Items.Stator, Rate(6.0)), (Items.AILimiter, Rate(4.0))],
        [(Items.ElectromagneticControlRod, Rate(4.0))],
    )
    UraniumFuelRod = Recipe(
        "Uranium Fuel Rod",
        [(Items.EncasedUraniumCell, Rate(20.0)), (Items.EncasedIndustrialBeam, Rate(1.2)), (Items.ElectromagneticControlRod, Rate(2.0))],
        [(Items.UraniumFuelRod, Rate(0.4))],
    )
    MagneticFieldGenerator = Recipe(
        "Magnetic Field Generator",
        [(Items.VersatileFramework, Rate(2.5)), (Items.ElectromagneticControlRod, Rate(1.0))],
        [(Items.MagneticFieldGenerator, Rate(1.0))],
    )
    SloppyAlumina = Recipe(
        "Alternate: Sloppy Alumina",
        [(Items.Bauxite, Rate(200.0)), (Items.Water, Rate(200.0))],
        [(Items.AluminaSolution, Rate(240.0))],
    )
    RadioControlSystem = Recipe(
        "Alternate: Radio Control System",
        [(Items.CrystalOscillator, Rate(1.5)), (Items.CircuitBoard, Rate(15.0)), (Items.AluminumCasing, Rate(90.0)), (Items.Rubber, Rate(45.0))],
        [(Items.RadioControlUnit, Rate(4.5))],
    )
    PlutoniumFuelUnit = Recipe(
        "Alternate: Plutonium Fuel Unit",
        [(Items.EncasedPlutoniumCell, Rate(10.0)), (Items.PressureConversionCube, Rate(0.5))],
        [(Items.PlutoniumFuelRod, Rate(0.5))],
    )
    OCSupercomputer = Recipe(
        "Alternate: OC Supercomputer",
        [(Items.RadioControlUnit, Rate(6.0)), (Items.CoolingSystem, Rate(6.0))],
        [(Items.Supercomputer, Rate(3.0))],
    )
    HeatSink = Recipe(
        "Heat Sink",
        [(Items.AlcladAluminumSheet, Rate(37.5)), (Items.CopperSheet, Rate(22.5))],
        [(Items.HeatSink, Rate(7.5))],
    )
    FusedModularFrame = Recipe(
        "Fused Modular Frame",
        [(Items.HeavyModularFrame, Rate(1.5)), (Items.AluminumCasing, Rate(75.0)), (Items.NitrogenGas, Rate(37.5))],
        [(Items.FusedModularFrame, Rate(1.5))],
    )
    EmptyFluidTank = Recipe(
        "Empty Fluid Tank",
        [(Items.AluminumIngot, Rate(60.0))],
        [(Items.EmptyFluidTank, Rate(60.0))],
    )
    PackagedNitrogenGas = Recipe(
        "Packaged Nitrogen Gas",
        [(Items.NitrogenGas, Rate(240.0)), (Items.EmptyFluidTank, Rate(60.0))],
        [(Items.PackagedNitrogenGas, Rate(60.0))],
    )
    UnpackageNitrogenGas = Recipe(
        "Unpackage Nitrogen Gas",
        [(Items.PackagedNitrogenGas, Rate(60.0))],
        [(Items.NitrogenGas, Rate(240.0)), (Items.EmptyFluidTank, Rate(60.0))],
    )
    InstantScrap = Recipe(
        "Alternate: Instant Scrap",
        [(Items.Bauxite, Rate(150.0)), (Items.Coal, Rate(100.0)), (Items.SulfuricAcid, Rate(50.0)), (Items.Water, Rate(60.0))],
        [(Items.AluminumScrap, Rate(300.0)), (Items.Water, Rate(50.0))],
    )
    InstantPlutoniumCell = Recipe(
        "Alternate: Instant Plutonium Cell",
        [(Items.NonFissileUranium, Rate(75.0)), (Items.AluminumCasing, Rate(10.0))],
        [(Items.EncasedPlutoniumCell, Rate(10.0))],
    )
    HeatFusedFrame = Recipe(
        "Alternate: Heat-Fused Frame",
        [(Items.HeavyModularFrame, Rate(3.0)), (Items.AluminumIngot, Rate(150.0)), (Items.NitricAcid, Rate(24.0)), (Items.Fuel, Rate(30.0))],
        [(Items.FusedModularFrame, Rate(3.0))],
    )
    FertileUranium = Recipe(
        "Alternate: Fertile Uranium",
        [(Items.Uranium, Rate(25.0)), (Items.UraniumWaste, Rate(25.0)), (Items.NitricAcid, Rate(15.0)), (Items.SulfuricAcid, Rate(25.0))],
        [(Items.NonFissileUranium, Rate(100.0)), (Items.Water, Rate(40.0))],
    )
    ElectricMotor = Recipe(
        "Alternate: Electric Motor",
        [(Items.ElectromagneticControlRod, Rate(3.75)), (Items.Rotor, Rate(7.5))],
        [(Items.Motor, Rate(7.5))],
    )
    DilutedFuel = Recipe(
        "Alternate: Diluted Fuel",
        [(Items.HeavyOilResidue, Rate(50.0)), (Items.Water, Rate(100.0))],
        [(Items.Fuel, Rate(100.0))],
    )
    CoolingDevice = Recipe(
        "Alternate: Cooling Device",
        [(Items.HeatSink, Rate(10.0)), (Items.Motor, Rate(2.5)), (Items.NitrogenGas, Rate(60.0))],
        [(Items.CoolingSystem, Rate(5.0))],
    )
    ClassicBattery = Recipe(
        "Alternate: Classic Battery",
        [(Items.Sulfur, Rate(45.0)), (Items.AlcladAluminumSheet, Rate(52.5)), (Items.Plastic, Rate(60.0)), (Items.Wire, Rate(90.0))],
        [(Items.Battery, Rate(30.0))],
    )
    AutomatedMiner = Recipe(
        "Alternate: Automated Miner",
        [(Items.SteelPipe, Rate(4.0)), (Items.IronPlate, Rate(4.0))],
        [(Items.PortableMiner, Rate(1.0))],
    )
    AlcladCasing = Recipe(
        "Alternate: Alclad Casing",
        [(Items.AluminumIngot, Rate(150.0)), (Items.CopperIngot, Rate(75.0))],
        [(Items.AluminumCasing, Rate(112.5))],
    )
    MoldedSteelPipe = Recipe(
        "Alternate: Molded Steel Pipe",
        [(Items.SteelIngot, Rate(50.0)), (Items.Concrete, Rate(30.0))],
        [(Items.SteelPipe, Rate(50.0))],
    )
    IronPipe = Recipe(
        "Alternate: Iron Pipe",
        [(Items.IronIngot, Rate(100.0))],
        [(Items.SteelPipe, Rate(25.0))],
    )
    SteelCastPlate = Recipe(
        "Alternate: Steel Cast Plate",
        [(Items.IronIngot, Rate(15.0)), (Items.SteelIngot, Rate(15.0))],
        [(Items.IronPlate, Rate(45.0))],
    )
    MoldedBeam = Recipe(
        "Alternate: Molded Beam",
        [(Items.SteelIngot, Rate(120.0)), (Items.Concrete, Rate(80.0))],
        [(Items.SteelBeam, Rate(45.0))],
    )
    AluminumBeam = Recipe(
        "Alternate: Aluminum Beam",
        [(Items.AluminumIngot, Rate(22.5))],
        [(Items.SteelBeam, Rate(22.5))],
    )
    AluminumRod = Recipe(
        "Alternate: Aluminum Rod",
        [(Items.AluminumIngot, Rate(7.5))],
        [(Items.IronRod, Rate(52.5))],
    )
    PlasticAILimiter = Recipe(
        "Alternate: Plastic AI Limiter",
        [(Items.Quickwire, Rate(120.0)), (Items.Plastic, Rate(28.0))],
        [(Items.AILimiter, Rate(8.0))],
    )
    DistilledSilica = Recipe(
        "Alternate: Distilled Silica",
        [(Items.DissolvedSilica, Rate(120.0)), (Items.Limestone, Rate(50.0)), (Items.Water, Rate(100.0))],
        [(Items.Silica, Rate(270.0)), (Items.Water, Rate(80.0))],
    )
    QuartzPurification = Recipe(
        "Alternate: Quartz Purification",
        [(Items.RawQuartz, Rate(120.0)), (Items.NitricAcid, Rate(10.0))],
        [(Items.QuartzCrystal, Rate(75.0)), (Items.DissolvedSilica, Rate(60.0))],
    )
    FusedQuartzCrystal = Recipe(
        "Alternate: Fused Quartz Crystal",
        [(Items.RawQuartz, Rate(75.0)), (Items.Coal, Rate(36.0))],
        [(Items.QuartzCrystal, Rate(54.0))],
    )
    LeachedIroningot = Recipe(
        "Alternate: Leached Iron ingot",
        [(Items.IronOre, Rate(50.0)), (Items.SulfuricAcid, Rate(10.0))],
        [(Items.IronIngot, Rate(100.0))],
    )
    BasicIronIngot = Recipe(
        "Alternate: Basic Iron Ingot",
        [(Items.IronOre, Rate(25.0)), (Items.Limestone, Rate(40.0))],
        [(Items.IronIngot, Rate(50.0))],
    )
    TemperedCopperIngot = Recipe(
        "Alternate: Tempered Copper Ingot",
        [(Items.CopperOre, Rate(25.0)), (Items.PetroleumCoke, Rate(40.0))],
        [(Items.CopperIngot, Rate(60.0))],
    )
    LeachedCopperIngot = Recipe(
        "Alternate: Leached Copper Ingot",
        [(Items.CopperOre, Rate(45.0)), (Items.SulfuricAcid, Rate(25.0))],
        [(Items.CopperIngot, Rate(110.0))],
    )
    TemperedCateriumIngot = Recipe(
        "Alternate: Tempered Caterium Ingot",
        [(Items.CateriumOre, Rate(45.0)), (Items.PetroleumCoke, Rate(15.0))],
        [(Items.CateriumIngot, Rate(22.5))],
    )
    LeachedCateriumIngot = Recipe(
        "Alternate: Leached Caterium Ingot",
        [(Items.CateriumOre, Rate(54.0)), (Items.SulfuricAcid, Rate(30.0))],
        [(Items.CateriumIngot, Rate(36.0))],
    )
    CateriumWire = Recipe(
        "Alternate: Caterium Wire",
        [(Items.CateriumIngot, Rate(15.0))],
        [(Items.Wire, Rate(120.0))],
    )
    IronWire = Recipe(
        "Alternate: Iron Wire",
        [(Items.IronIngot, Rate(12.5))],
        [(Items.Wire, Rate(22.5))],
    )
    InfusedUraniumCell = Recipe(
        "Alternate: Infused Uranium Cell",
        [(Items.Uranium, Rate(25.0)), (Items.Silica, Rate(15.0)), (Items.Sulfur, Rate(25.0)), (Items.Quickwire, Rate(75.0))],
        [(Items.EncasedUraniumCell, Rate(20.0))],
    )
    CateriumIngot = Recipe(
        "Caterium Ingot",
        [(Items.CateriumOre, Rate(45.0))],
        [(Items.CateriumIngot, Rate(15.0))],
    )
    TurboElectricMotor = Recipe(
        "Alternate: Turbo Electric Motor",
        [(Items.Motor, Rate(6.5625)), (Items.RadioControlUnit, Rate(8.4375)), (Items.ElectromagneticControlRod, Rate(4.6875)), (Items.Rotor, Rate(6.5625))],
        [(Items.TurboMotor, Rate(2.8125))],
    )
    TurboMotor = Recipe(
        "Turbo Motor",
        [(Items.CoolingSystem, Rate(7.5)), (Items.RadioControlUnit, Rate(3.75)), (Items.Motor, Rate(7.5)), (Items.Rubber, Rate(45.0))],
        [(Items.TurboMotor, Rate(1.875))],
    )
    ThermalPropulsionRocket = Recipe(
        "Thermal Propulsion Rocket",
        [(Items.ModularEngine, Rate(2.5)), (Items.TurboMotor, Rate(1.0)), (Items.CoolingSystem, Rate(3.0)), (Items.FusedModularFrame, Rate(1.0))],
        [(Items.ThermalPropulsionRocket, Rate(1.0))],
    )
    SteelScrew = Recipe(
        "Alternate: Steel Screw",
        [(Items.SteelBeam, Rate(5.0))],
        [(Items.Screw, Rate(260.0))],
    )
    Screw = Recipe(
        "Screw",
        [(Items.IronRod, Rate(10.0))],
        [(Items.Screw, Rate(40.0))],
    )
    StitchedIronPlate = Recipe(
        "Alternate: Stitched Iron Plate",
        [(Items.IronPlate, Rate(18.75)), (Items.Wire, Rate(37.5))],
        [(Items.ReinforcedIronPlate, Rate(5.625))],
    )
    BoltedIronPlate = Recipe(
        "Alternate: Bolted Iron Plate",
        [(Items.IronPlate, Rate(90.0)), (Items.Screw, Rate(250.0))],
        [(Items.ReinforcedIronPlate, Rate(15.0))],
    )
    RadioConnectionUnit = Recipe(
        "Alternate: Radio Connection Unit",
        [(Items.HeatSink, Rate(15.0)), (Items.HighSpeedConnector, Rate(7.5)), (Items.QuartzCrystal, Rate(45.0))],
        [(Items.RadioControlUnit, Rate(3.75))],
    )
    Quickwire = Recipe(
        "Quickwire",
        [(Items.CateriumIngot, Rate(12.0))],
        [(Items.Quickwire, Rate(60.0))],
    )
    RecycledPlastic = Recipe(
        "Alternate: Recycled Plastic",
        [(Items.Rubber, Rate(30.0)), (Items.Fuel, Rate(30.0))],
        [(Items.Plastic, Rate(60.0))],
    )
    UraniumFuelUnit = Recipe(
        "Alternate: Uranium Fuel Unit",
        [(Items.EncasedUraniumCell, Rate(20.0)), (Items.ElectromagneticControlRod, Rate(2.0)), (Items.CrystalOscillator, Rate(0.6)), (Items.Rotor, Rate(2.0))],
        [(Items.UraniumFuelRod, Rate(0.6))],
    )
    RigorMotor = Recipe(
        "Alternate: Rigor Motor",
        [(Items.Rotor, Rate(3.75)), (Items.Stator, Rate(3.75)), (Items.CrystalOscillator, Rate(1.25))],
        [(Items.Motor, Rate(7.5))],
    )
    CompactedSteelIngot = Recipe(
        "Alternate: Compacted Steel Ingot",
        [(Items.IronOre, Rate(5.0)), (Items.CompactedCoal, Rate(2.5))],
        [(Items.SteelIngot, Rate(10.0))],
    )
    SolidSteelIngot = Recipe(
        "Alternate: Solid Steel Ingot",
        [(Items.IronIngot, Rate(40.0)), (Items.Coal, Rate(40.0))],
        [(Items.SteelIngot, Rate(60.0))],
    )
    HeatExchanger = Recipe(
        "Alternate: Heat Exchanger",
        [(Items.AluminumCasing, Rate(30.0)), (Items.Rubber, Rate(30.0))],
        [(Items.HeatSink, Rate(10.0))],
    )
    FineBlackPowder = Recipe(
        "Alternate: Fine Black Powder",
        [(Items.Sulfur, Rate(7.5)), (Items.CompactedCoal, Rate(15.0))],
        [(Items.BlackPowder, Rate(45.0))],
    )
    ElectromagneticConnectionRod = Recipe(
        "Alternate: Electromagnetic Connection Rod",
        [(Items.Stator, Rate(8.0)), (Items.HighSpeedConnector, Rate(4.0))],
        [(Items.ElectromagneticControlRod, Rate(8.0))],
    )
    Concrete = Recipe(
        "Concrete",
        [(Items.Limestone, Rate(45.0))],
        [(Items.Concrete, Rate(15.0))],
    )
    CrystalComputer = Recipe(
        "Alternate: Crystal Computer",
        [(Items.CircuitBoard, Rate(5.0)), (Items.CrystalOscillator, Rate(1.6666666666666667))],
        [(Items.Computer, Rate(3.3333333333333335))],
    )
    CateriumComputer = Recipe(
        "Alternate: Caterium Computer",
        [(Items.CircuitBoard, Rate(15.0)), (Items.Quickwire, Rate(52.5)), (Items.Rubber, Rate(22.5))],
        [(Items.Computer, Rate(3.75))],
    )
    CateriumCircuitBoard = Recipe(
        "Alternate: Caterium Circuit Board",
        [(Items.Plastic, Rate(12.5)), (Items.Quickwire, Rate(37.5))],
        [(Items.CircuitBoard, Rate(8.75))],
    )
    SiliconCircuitBoard = Recipe(
        "Alternate: Silicon Circuit Board",
        [(Items.CopperSheet, Rate(27.5)), (Items.Silica, Rate(27.5))],
        [(Items.CircuitBoard, Rate(12.5))],
    )
    QuickwireCable = Recipe(
        "Alternate: Quickwire Cable",
        [(Items.Quickwire, Rate(7.5)), (Items.Rubber, Rate(5.0))],
        [(Items.Cable, Rate(27.5))],
    )
    InsulatedCable = Recipe(
        "Alternate: Insulated Cable",
        [(Items.Wire, Rate(45.0)), (Items.Rubber, Rate(30.0))],
        [(Items.Cable, Rate(100.0))],
    )
    Ficsonium = Recipe(
        "Ficsonium",
        [(Items.PlutoniumWaste, Rate(10.0)), (Items.SingularityCell, Rate(10.0)), (Items.DarkMatterResidue, Rate(200.0))],
        [(Items.Ficsonium, Rate(10.0))],
    )
    FicsoniumFuelRod = Recipe(
        "Ficsonium Fuel Rod",
        [(Items.Ficsonium, Rate(5.0)), (Items.ElectromagneticControlRod, Rate(5.0)), (Items.FicsiteTrigon, Rate(100.0)), (Items.ExcitedPhotonicMatter, Rate(50.0))],
        [(Items.FicsoniumFuelRod, Rate(2.5)), (Items.DarkMatterResidue, Rate(50.0))],
    )
    SingularityCell = Recipe(
        "Singularity Cell",
        [(Items.NuclearPasta, Rate(1.0)), (Items.DarkMatterCrystal, Rate(20.0)), (Items.IronPlate, Rate(100.0)), (Items.Concrete, Rate(200.0))],
        [(Items.SingularityCell, Rate(10.0))],
    )
    BallisticWarpDrive = Recipe(
        "Ballistic Warp Drive",
        [(Items.ThermalPropulsionRocket, Rate(1.0)), (Items.SingularityCell, Rate(5.0)), (Items.SuperpositionOscillator, Rate(2.0)), (Items.DarkMatterCrystal, Rate(40.0))],
        [(Items.BallisticWarpDrive, Rate(1.0))],
    )
    SolidBiofuel = Recipe(
        "Solid Biofuel",
        [(Items.Biomass, Rate(120.0))],
        [(Items.SolidBiofuel, Rate(60.0))],
    )
    HogProtein = Recipe(
        "Hog Protein",
        [(Items.HogRemains, Rate(20.0))],
        [(Items.AlienProtein, Rate(20.0))],
    )
    SpitterProtein = Recipe(
        "Spitter Protein",
        [(Items.SpitterRemains, Rate(20.0))],
        [(Items.AlienProtein, Rate(20.0))],
    )
    BiomassMycelia = Recipe(
        "Biomass (Mycelia)",
        [(Items.Mycelia, Rate(15.0))],
        [(Items.Biomass, Rate(150.0))],
    )
    PowerShard1 = Recipe(
        "Power Shard (1)",
        [(Items.BluePowerSlug, Rate(7.5))],
        [(Items.PowerShard, Rate(7.5))],
    )
    AlienPowerMatrix = Recipe(
        "Alien Power Matrix",
        [(Items.SAMFluctuator, Rate(12.5)), (Items.PowerShard, Rate(7.5)), (Items.SuperpositionOscillator, Rate(7.5)), (Items.ExcitedPhotonicMatter, Rate(60.0))],
        [(Items.AlienPowerMatrix, Rate(2.5)), (Items.DarkMatterResidue, Rate(60.0))],
    )
    StingerProtein = Recipe(
        "Stinger Protein",
        [(Items.StingerRemains, Rate(20.0))],
        [(Items.AlienProtein, Rate(20.0))],
    )
    HatcherProtein = Recipe(
        "Hatcher Protein",
        [(Items.HatcherRemains, Rate(20.0))],
        [(Items.AlienProtein, Rate(20.0))],
    )
    AlienDNACapsule = Recipe(
        "Alien DNA Capsule",
        [(Items.AlienProtein, Rate(10.0))],
        [(Items.AlienDNACapsule, Rate(10.0))],
    )
    BiomassAlienProtein = Recipe(
        "Biomass (Alien Protein)",
        [(Items.AlienProtein, Rate(15.0))],
        [(Items.Biomass, Rate(1500.0))],
    )
    PolyesterFabric = Recipe(
        "Alternate: Polyester Fabric",
        [(Items.PolymerResin, Rate(30.0)), (Items.Water, Rate(30.0))],
        [(Items.Fabric, Rate(30.0))],
    )
    Fabric = Recipe(
        "Fabric",
        [(Items.Mycelia, Rate(15.0)), (Items.Biomass, Rate(75.0))],
        [(Items.Fabric, Rate(15.0))],
    )
    SyntheticPowerShard = Recipe(
        "Synthetic Power Shard",
        [(Items.TimeCrystal, Rate(10.0)), (Items.DarkMatterCrystal, Rate(10.0)), (Items.QuartzCrystal, Rate(60.0)), (Items.ExcitedPhotonicMatter, Rate(60.0))],
        [(Items.PowerShard, Rate(5.0)), (Items.DarkMatterResidue, Rate(60.0))],
    )
    PowerShard5 = Recipe(
        "Power Shard (5)",
        [(Items.PurplePowerSlug, Rate(2.5))],
        [(Items.PowerShard, Rate(12.5))],
    )
    PowerShard2 = Recipe(
        "Power Shard (2)",
        [(Items.YellowPowerSlug, Rate(5.0))],
        [(Items.PowerShard, Rate(10.0))],
    )
    TurboRifleAmmo = Recipe(
        "Turbo Rifle Ammo",
        [(Items.RifleAmmo, Rate(125.0)), (Items.AluminumCasing, Rate(15.0)), (Items.Turbofuel, Rate(15.0))],
        [(Items.TurboRifleAmmo, Rate(250.0))],
    )
    SmokelessPowder = Recipe(
        "Smokeless Powder",
        [(Items.BlackPowder, Rate(20.0)), (Items.HeavyOilResidue, Rate(10.0))],
        [(Items.SmokelessPowder, Rate(20.0))],
    )
    BiomassLeaves = Recipe(
        "Biomass (Leaves)",
        [(Items.Leaves, Rate(120.0))],
        [(Items.Biomass, Rate(60.0))],
    )
    BiomassWood = Recipe(
        "Biomass (Wood)",
        [(Items.Wood, Rate(60.0))],
        [(Items.Biomass, Rate(300.0))],
    )
    ReinforcedIronPlate = Recipe(
        "Reinforced Iron Plate",
        [(Items.IronPlate, Rate(30.0)), (Items.Screw, Rate(60.0))],
        [(Items.ReinforcedIronPlate, Rate(5.0))],
    )
    Cable = Recipe(
        "Cable",
        [(Items.Wire, Rate(60.0))],
        [(Items.Cable, Rate(30.0))],
    )
    Wire = Recipe(
        "Wire",
        [(Items.CopperIngot, Rate(15.0))],
        [(Items.Wire, Rate(30.0))],
    )
    CopperIngot = Recipe(
        "Copper Ingot",
        [(Items.CopperOre, Rate(30.0))],
        [(Items.CopperIngot, Rate(30.0))],
    )
