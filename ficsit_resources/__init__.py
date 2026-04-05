from ficsit_resources.types import Item, Recipe, Rate
from ficsit_resources.items import Items
from ficsit_resources.recipes import Recipes

Items.UraniumWaste._attach_recipes(
    [],
    [Recipes.NonFissileUranium, Recipes.PlutoniumPellet, Recipes.FertileUranium],
)
Items.PlutoniumWaste._attach_recipes(
    [],
    [Recipes.Ficsonium],
)
Items.Concrete._attach_recipes(
    [Recipes.WetConcrete, Recipes.RubberConcrete, Recipes.FineConcrete, Recipes.Concrete],
    [Recipes.EncasedIndustrialBeam, Recipes.EncasedPlutoniumCell, Recipes.EncasedUraniumCell, Recipes.MoldedSteelPipe, Recipes.MoldedBeam, Recipes.EncasedIndustrialPipe, Recipes.HeavyEncasedFrame, Recipes.SingularityCell],
)
Items.Silica._attach_recipes(
    [Recipes.AluminaSolution, Recipes.Silica, Recipes.DistilledSilica, Recipes.CheapSilica],
    [Recipes.AluminumIngot, Recipes.NonFissileUranium, Recipes.InfusedUraniumCell, Recipes.SiliconHighSpeedConnector, Recipes.FineConcrete, Recipes.SiliconCircuitBoard, Recipes.BladeRunners],
)
Items.IronPlate._attach_recipes(
    [Recipes.IronPlate, Recipes.CoatedIronPlate, Recipes.SteelCastPlate],
    [Recipes.CoatedIronCanister, Recipes.AdheredIronPlate, Recipes.NitricAcid, Recipes.AutomatedMiner, Recipes.StitchedIronPlate, Recipes.BoltedIronPlate, Recipes.SingularityCell, Recipes.Jetpack, Recipes.GasFilter, Recipes.ReinforcedIronPlate, Recipes.PortableMiner],
)
Items.SteelBeam._attach_recipes(
    [Recipes.SteelBeam, Recipes.MoldedBeam, Recipes.AluminumBeam],
    [Recipes.VersatileFramework, Recipes.EncasedIndustrialBeam, Recipes.FlexibleFramework, Recipes.PlutoniumFuelRod, Recipes.SteelScrew, Recipes.NobeliskDetonator],
)
Items.AluminumIngot._attach_recipes(
    [Recipes.PureAluminumIngot, Recipes.AluminumIngot],
    [Recipes.FicsiteIngotFromAluminum, Recipes.AluminumCasing, Recipes.AlcladAluminumSheet, Recipes.EmptyFluidTank, Recipes.HeatFusedFrame, Recipes.AlcladCasing, Recipes.AluminumBeam, Recipes.AluminumRod],
)
Items.Battery._attach_recipes(
    [Recipes.Battery, Recipes.ClassicBattery],
    [Recipes.SuperStateComputer],
)
Items.PackagedFuel._attach_recipes(
    [Recipes.PackagedFuel, Recipes.DilutedPackagedFuel],
    [Recipes.UnpackageFuel],
)
Items.PackagedIonizedFuel._attach_recipes(
    [Recipes.PackagedIonizedFuel],
    [Recipes.UnpackageIonizedFuel],
)
Items.PackagedRocketFuel._attach_recipes(
    [Recipes.PackagedRocketFuel],
    [Recipes.UnpackageRocketFuel, Recipes.DarkIonFuel],
)
Items.PackagedTurbofuel._attach_recipes(
    [Recipes.PackagedTurbofuel],
    [Recipes.TurboDiamonds, Recipes.UnpackageTurbofuel],
)
Items.IodineInfusedFilter._attach_recipes(
    [Recipes.IodineInfusedFilter],
    [],
)
Items.CompactedCoal._attach_recipes(
    [Recipes.NitroRocketFuel, Recipes.RocketFuel, Recipes.DarkIonFuel, Recipes.IonizedFuel, Recipes.CompactedCoal],
    [Recipes.Turbofuel, Recipes.TurboHeavyFuel, Recipes.CompactedSteelIngot, Recipes.FineBlackPowder],
)
Items.PackagedHeavyOilResidue._attach_recipes(
    [Recipes.PackagedHeavyOilResidue],
    [Recipes.UnpackageHeavyOilResidue],
)
Items.PetroleumCoke._attach_recipes(
    [Recipes.PetroleumCoke],
    [Recipes.PetroleumDiamonds, Recipes.ElectrodeCircuitBoard, Recipes.ElectrodeAluminumScrap, Recipes.CokeSteelIngot, Recipes.TurboBlendFuel, Recipes.TemperedCopperIngot, Recipes.TemperedCateriumIngot],
)
Items.PackagedOil._attach_recipes(
    [Recipes.PackagedOil],
    [Recipes.UnpackageOil],
)
Items.IronRod._attach_recipes(
    [Recipes.IronRod, Recipes.SteelRod, Recipes.AluminumRod],
    [Recipes.XenoZapper, Recipes.ModularFrame, Recipes.Rotor, Recipes.XenoBasher, Recipes.Chainsaw, Recipes.IronRebar, Recipes.RebarGun, Recipes.Zipline, Recipes.FactoryCart, Recipes.GoldenFactoryCart, Recipes.Screw, Recipes.PortableMiner],
)
Items.Wire._attach_recipes(
    [Recipes.FusedWire, Recipes.CateriumWire, Recipes.IronWire, Recipes.Wire],
    [Recipes.XenoZapper, Recipes.SAMFluctuator, Recipes.AutomatedSpeedWiring, Recipes.Stator, Recipes.CoatedCable, Recipes.SuperStateComputer, Recipes.ClassicBattery, Recipes.SteelRotor, Recipes.StitchedIronPlate, Recipes.InsulatedCable, Recipes.Jetpack, Recipes.XenoBasher, Recipes.ObjectScanner, Recipes.Cable],
)
Items.Cable._attach_recipes(
    [Recipes.CoatedCable, Recipes.QuickwireCable, Recipes.InsulatedCable, Recipes.Cable],
    [Recipes.XenoZapper, Recipes.CrystalOscillator, Recipes.AutomatedWiring, Recipes.Computer, Recipes.HighSpeedConnector, Recipes.Chainsaw, Recipes.Zipline, Recipes.Parachute, Recipes.NobeliskDetonator],
)
Items.IronIngot._attach_recipes(
    [Recipes.IronIngot, Recipes.PureIronIngot, Recipes.LeachedIroningot, Recipes.BasicIronIngot, Recipes.IronAlloyIngot],
    [Recipes.IronPlate, Recipes.IronRod, Recipes.FicsiteIngotFromIron, Recipes.CoatedIronPlate, Recipes.IronPipe, Recipes.SteelCastPlate, Recipes.IronWire, Recipes.CastScrew, Recipes.SolidSteelIngot],
)
Items.ReinforcedIronPlate._attach_recipes(
    [Recipes.AdheredIronPlate, Recipes.StitchedIronPlate, Recipes.BoltedIronPlate, Recipes.ReinforcedIronPlate],
    [Recipes.XenoZapper, Recipes.CrystalOscillator, Recipes.PlasticSmartPlating, Recipes.ModularFrame, Recipes.SmartPlating, Recipes.BoltedFrame, Recipes.SteeledFrame, Recipes.Chainsaw, Recipes.ObjectScanner, Recipes.RebarGun, Recipes.FactoryCart],
)
Items.Rotor._attach_recipes(
    [Recipes.CopperRotor, Recipes.Rotor, Recipes.SteelRotor],
    [Recipes.PlasticSmartPlating, Recipes.Motor, Recipes.SmartPlating, Recipes.ElectricMotor, Recipes.TurboElectricMotor, Recipes.UraniumFuelUnit, Recipes.RigorMotor, Recipes.BladeRunners, Recipes.FactoryCart, Recipes.GoldenFactoryCart],
)
Items.Fuel._attach_recipes(
    [Recipes.Fuel, Recipes.ResidualFuel, Recipes.UnpackageFuel, Recipes.DilutedFuel],
    [Recipes.NitroRocketFuel, Recipes.Turbofuel, Recipes.PackagedFuel, Recipes.RecycledRubber, Recipes.TurboBlendFuel, Recipes.HeatFusedFrame, Recipes.RecycledPlastic],
)
Items.RocketFuel._attach_recipes(
    [Recipes.NitroRocketFuel, Recipes.RocketFuel, Recipes.UnpackageRocketFuel],
    [Recipes.PackagedRocketFuel, Recipes.IonizedFuel],
)
Items.CopperSheet._attach_recipes(
    [Recipes.SteamedCopperSheet, Recipes.CopperSheet],
    [Recipes.CircuitBoard, Recipes.AILimiter, Recipes.CopperRotor, Recipes.CoatedIronCanister, Recipes.HeatSink, Recipes.SiliconCircuitBoard, Recipes.GasMask, Recipes.RifleAmmo],
)
Items.ModularFrame._attach_recipes(
    [Recipes.ModularFrame, Recipes.BoltedFrame, Recipes.SteeledFrame],
    [Recipes.VersatileFramework, Recipes.HeavyFlexibleFrame, Recipes.HeavyModularFrame, Recipes.FlexibleFramework, Recipes.HeavyEncasedFrame, Recipes.XenoBasher, Recipes.BladeRunners],
)
Items.Screw._attach_recipes(
    [Recipes.SteelScrew, Recipes.CastScrew, Recipes.Screw],
    [Recipes.HeavyFlexibleFrame, Recipes.HeavyModularFrame, Recipes.CopperRotor, Recipes.Rotor, Recipes.BoltedFrame, Recipes.BoltedIronPlate, Recipes.Chainsaw, Recipes.ObjectScanner, Recipes.RebarGun, Recipes.Rifle, Recipes.ReinforcedIronPlate],
)
Items.NitricAcid._attach_recipes(
    [Recipes.NitricAcid, Recipes.UnpackageNitricAcid],
    [Recipes.RocketFuel, Recipes.NonFissileUranium, Recipes.PackagedNitricAcid, Recipes.HeatFusedFrame, Recipes.FertileUranium, Recipes.QuartzPurification],
)
Items.Turbofuel._attach_recipes(
    [Recipes.Turbofuel, Recipes.UnpackageTurbofuel, Recipes.TurboHeavyFuel, Recipes.TurboBlendFuel],
    [Recipes.RocketFuel, Recipes.PackagedTurbofuel, Recipes.TurboRifleAmmo],
)
Items.EmptyFluidTank._attach_recipes(
    [Recipes.UnpackageRocketFuel, Recipes.UnpackageIonizedFuel, Recipes.UnpackageNitricAcid, Recipes.EmptyFluidTank, Recipes.UnpackageNitrogenGas],
    [Recipes.PackagedRocketFuel, Recipes.PackagedIonizedFuel, Recipes.PackagedNitricAcid, Recipes.PackagedNitrogenGas],
)
Items.CrystalOscillator._attach_recipes(
    [Recipes.CrystalOscillator, Recipes.InsulatedCrystalOscillator],
    [Recipes.SuperpositionOscillator, Recipes.RadioControlUnit, Recipes.RadioControlSystem, Recipes.UraniumFuelUnit, Recipes.RigorMotor, Recipes.CrystalComputer, Recipes.PulseNobelisk],
)
Items.Motor._attach_recipes(
    [Recipes.Motor, Recipes.ElectricMotor, Recipes.RigorMotor],
    [Recipes.ModularEngine, Recipes.TurboPressureMotor, Recipes.CoolingDevice, Recipes.TurboElectricMotor, Recipes.TurboMotor, Recipes.Hoverpack, Recipes.Jetpack, Recipes.Rifle],
)
Items.DarkMatterCrystal._attach_recipes(
    [Recipes.DarkMatterCrystal, Recipes.DarkMatterTrap, Recipes.DarkMatterCrystallization],
    [Recipes.DarkIonFuel, Recipes.SuperpositionOscillator, Recipes.SingularityCell, Recipes.BallisticWarpDrive, Recipes.SyntheticPowerShard],
)
Items.IonizedFuel._attach_recipes(
    [Recipes.DarkIonFuel, Recipes.IonizedFuel, Recipes.UnpackageIonizedFuel],
    [Recipes.PackagedIonizedFuel],
)
Items.Supercomputer._attach_recipes(
    [Recipes.Supercomputer, Recipes.SuperStateComputer, Recipes.OCSupercomputer],
    [Recipes.NeuralQuantumProcessor, Recipes.AssemblyDirectorSystem],
)
Items.CoolingSystem._attach_recipes(
    [Recipes.CoolingSystem, Recipes.CoolingDevice],
    [Recipes.OCSupercomputer, Recipes.TurboMotor, Recipes.ThermalPropulsionRocket],
)
Items.FicsiteTrigon._attach_recipes(
    [Recipes.FicsiteTrigon],
    [Recipes.NeuralQuantumProcessor, Recipes.BiochemicalSculptor, Recipes.FicsoniumFuelRod],
)
Items.TurboMotor._attach_recipes(
    [Recipes.TurboPressureMotor, Recipes.TurboElectricMotor, Recipes.TurboMotor],
    [Recipes.ThermalPropulsionRocket],
)
Items.TimeCrystal._attach_recipes(
    [Recipes.TimeCrystal],
    [Recipes.NeuralQuantumProcessor, Recipes.DarkMatterTrap, Recipes.SyntheticPowerShard],
)
Items.DarkMatterResidue._attach_recipes(
    [Recipes.DarkMatterResidue, Recipes.SuperpositionOscillator, Recipes.NeuralQuantumProcessor, Recipes.AIExpansionServer, Recipes.FicsoniumFuelRod, Recipes.AlienPowerMatrix, Recipes.SyntheticPowerShard],
    [Recipes.DarkMatterCrystal, Recipes.DarkMatterTrap, Recipes.DarkMatterCrystallization, Recipes.Ficsonium],
)
Items.ReanimatedSAM._attach_recipes(
    [Recipes.ReanimatedSAM],
    [Recipes.DarkMatterResidue, Recipes.SAMFluctuator, Recipes.FicsiteIngotFromIron, Recipes.FicsiteIngotFromAluminum, Recipes.FicsiteIngotFromCaterium, Recipes.BauxiteFromCaterium, Recipes.BauxiteFromCopper, Recipes.CateriumOreFromCopper, Recipes.CateriumOreFromQuartz, Recipes.CoalFromIron, Recipes.CoalFromLimestone, Recipes.CopperOreFromQuartz, Recipes.CopperOreFromSulfur, Recipes.IronOreFromLimestone, Recipes.LimestoneFromSulfur, Recipes.NitrogenGasFromBauxite, Recipes.NitrogenGasFromCaterium, Recipes.RawQuartzFromBauxite, Recipes.RawQuartzFromCoal, Recipes.SulfurFromCoal, Recipes.SulfurFromIron, Recipes.UraniumOreFromBauxite],
)
Items.ExcitedPhotonicMatter._attach_recipes(
    [Recipes.ExcitedPhotonicMatter],
    [Recipes.SuperpositionOscillator, Recipes.NeuralQuantumProcessor, Recipes.AIExpansionServer, Recipes.FicsoniumFuelRod, Recipes.AlienPowerMatrix, Recipes.SyntheticPowerShard],
)
Items.Diamonds._attach_recipes(
    [Recipes.TurboDiamonds, Recipes.Diamonds, Recipes.PinkDiamonds, Recipes.PetroleumDiamonds, Recipes.OilBasedDiamonds, Recipes.CloudyDiamonds],
    [Recipes.DarkMatterCrystal, Recipes.TimeCrystal],
)
Items.AlcladAluminumSheet._attach_recipes(
    [Recipes.AlcladAluminumSheet],
    [Recipes.SuperpositionOscillator, Recipes.HeatSink, Recipes.ClassicBattery, Recipes.Hoverpack, Recipes.HazmatSuit],
)
Items.SuperpositionOscillator._attach_recipes(
    [Recipes.SuperpositionOscillator],
    [Recipes.AIExpansionServer, Recipes.BallisticWarpDrive, Recipes.AlienPowerMatrix],
)
Items.NeuralQuantumProcessor._attach_recipes(
    [Recipes.NeuralQuantumProcessor],
    [Recipes.AIExpansionServer],
)
Items.AIExpansionServer._attach_recipes(
    [Recipes.AIExpansionServer],
    [],
)
Items.MagneticFieldGenerator._attach_recipes(
    [Recipes.MagneticFieldGenerator],
    [Recipes.AIExpansionServer],
)
Items.SAMFluctuator._attach_recipes(
    [Recipes.SAMFluctuator],
    [Recipes.AlienPowerMatrix],
)
Items.SteelPipe._attach_recipes(
    [Recipes.SteelPipe, Recipes.MoldedSteelPipe, Recipes.IronPipe],
    [Recipes.SAMFluctuator, Recipes.Stator, Recipes.HeavyModularFrame, Recipes.AutomatedMiner, Recipes.QuickwireStator, Recipes.SteelRotor, Recipes.EncasedIndustrialPipe, Recipes.SteeledFrame, Recipes.HeavyEncasedFrame, Recipes.Jetpack, Recipes.GasMask, Recipes.ExplosiveRebar, Recipes.Rifle, Recipes.Nobelisk],
)
Items.FusedModularFrame._attach_recipes(
    [Recipes.FusedModularFrame, Recipes.HeatFusedFrame],
    [Recipes.PressureConversionCube, Recipes.ThermalPropulsionRocket],
)
Items.RadioControlUnit._attach_recipes(
    [Recipes.RadioControlUnit, Recipes.RadioControlSystem, Recipes.RadioConnectionUnit],
    [Recipes.PressureConversionCube, Recipes.OCSupercomputer, Recipes.TurboElectricMotor, Recipes.TurboMotor],
)
Items.FicsiteIngot._attach_recipes(
    [Recipes.FicsiteIngotFromIron, Recipes.FicsiteIngotFromAluminum, Recipes.FicsiteIngotFromCaterium],
    [Recipes.FicsiteTrigon],
)
Items.BiochemicalSculptor._attach_recipes(
    [Recipes.BiochemicalSculptor],
    [],
)
Items.AssemblyDirectorSystem._attach_recipes(
    [Recipes.AssemblyDirectorSystem],
    [Recipes.BiochemicalSculptor],
)
Items.CateriumIngot._attach_recipes(
    [Recipes.PureCateriumIngot, Recipes.TemperedCateriumIngot, Recipes.LeachedCateriumIngot, Recipes.CateriumIngot],
    [Recipes.FicsiteIngotFromCaterium, Recipes.FusedWire, Recipes.CateriumWire, Recipes.FusedQuickwire, Recipes.Quickwire, Recipes.GoldenFactoryCart],
)
Items.EmptyCanister._attach_recipes(
    [Recipes.UnpackageTurbofuel, Recipes.SteelCanister, Recipes.EmptyCanister, Recipes.UnpackageLiquidBiofuel, Recipes.UnpackageFuel, Recipes.UnpackageOil, Recipes.UnpackageHeavyOilResidue, Recipes.UnpackageWater, Recipes.UnpackageAluminaSolution, Recipes.CoatedIronCanister, Recipes.UnpackageSulfuricAcid],
    [Recipes.PackagedTurbofuel, Recipes.PackagedFuel, Recipes.PackagedLiquidBiofuel, Recipes.PackagedOil, Recipes.PackagedHeavyOilResidue, Recipes.PackagedWater, Recipes.PackagedAluminaSolution, Recipes.PackagedSulfuricAcid],
)
Items.CircuitBoard._attach_recipes(
    [Recipes.CircuitBoard, Recipes.ElectrodeCircuitBoard, Recipes.CateriumCircuitBoard, Recipes.SiliconCircuitBoard],
    [Recipes.Computer, Recipes.AdaptiveControlUnit, Recipes.HighSpeedConnector, Recipes.RadioControlSystem, Recipes.SiliconHighSpeedConnector, Recipes.CrystalComputer, Recipes.CateriumComputer],
)
Items.Plastic._attach_recipes(
    [Recipes.Plastic, Recipes.ResidualPlastic, Recipes.RecycledPlastic],
    [Recipes.CircuitBoard, Recipes.EmptyCanister, Recipes.RecycledRubber, Recipes.PlasticSmartPlating, Recipes.Computer, Recipes.CoatedIronPlate, Recipes.Supercomputer, Recipes.ClassicBattery, Recipes.PlasticAILimiter, Recipes.CateriumCircuitBoard, Recipes.HazmatSuit],
)
Items.EncasedIndustrialBeam._attach_recipes(
    [Recipes.EncasedIndustrialBeam, Recipes.EncasedIndustrialPipe],
    [Recipes.HeavyFlexibleFrame, Recipes.HeavyModularFrame, Recipes.UraniumFuelRod, Recipes.HeavyEncasedFrame],
)
Items.Rubber._attach_recipes(
    [Recipes.Rubber, Recipes.ResidualRubber, Recipes.RecycledRubber],
    [Recipes.RubberConcrete, Recipes.HeavyFlexibleFrame, Recipes.ModularEngine, Recipes.FlexibleFramework, Recipes.ElectrodeCircuitBoard, Recipes.AdheredIronPlate, Recipes.CoolingSystem, Recipes.RadioControlSystem, Recipes.TurboMotor, Recipes.RecycledPlastic, Recipes.HeatExchanger, Recipes.InsulatedCrystalOscillator, Recipes.CateriumComputer, Recipes.QuickwireCable, Recipes.InsulatedCable, Recipes.HazmatSuit, Recipes.Rifle],
)
Items.PolymerResin._attach_recipes(
    [Recipes.Fuel, Recipes.PolymerResin, Recipes.HeavyOilResidue],
    [Recipes.ResidualPlastic, Recipes.ResidualRubber, Recipes.PolyesterFabric],
)
Items.HeavyOilResidue._attach_recipes(
    [Recipes.Plastic, Recipes.Rubber, Recipes.UnpackageHeavyOilResidue, Recipes.PolymerResin, Recipes.HeavyOilResidue],
    [Recipes.PetroleumCoke, Recipes.ResidualFuel, Recipes.TurboHeavyFuel, Recipes.PackagedHeavyOilResidue, Recipes.DilutedPackagedFuel, Recipes.CoatedCable, Recipes.TurboBlendFuel, Recipes.DilutedFuel, Recipes.SmokelessPowder],
)
Items.QuartzCrystal._attach_recipes(
    [Recipes.PureQuartzCrystal, Recipes.QuartzCrystal, Recipes.QuartzPurification, Recipes.FusedQuartzCrystal],
    [Recipes.PinkDiamonds, Recipes.CrystalOscillator, Recipes.RadioConnectionUnit, Recipes.InsulatedCrystalOscillator, Recipes.SyntheticPowerShard, Recipes.ShatterRebar],
)
Items.SteelIngot._attach_recipes(
    [Recipes.SteelIngot, Recipes.CokeSteelIngot, Recipes.CompactedSteelIngot, Recipes.SolidSteelIngot],
    [Recipes.SteelRod, Recipes.SteelBeam, Recipes.SteelPipe, Recipes.SteelCanister, Recipes.MoldedSteelPipe, Recipes.SteelCastPlate, Recipes.MoldedBeam],
)
Items.VersatileFramework._attach_recipes(
    [Recipes.VersatileFramework, Recipes.FlexibleFramework],
    [Recipes.MagneticFieldGenerator],
)
Items.PackagedWater._attach_recipes(
    [Recipes.PackagedWater],
    [Recipes.UnpackageWater, Recipes.DilutedPackagedFuel],
)
Items.CopperIngot._attach_recipes(
    [Recipes.PureCopperIngot, Recipes.CopperAlloyIngot, Recipes.TemperedCopperIngot, Recipes.LeachedCopperIngot, Recipes.CopperIngot],
    [Recipes.SteamedCopperSheet, Recipes.AlcladAluminumSheet, Recipes.FusedWire, Recipes.CopperSheet, Recipes.CopperPowder, Recipes.AlcladCasing, Recipes.FusedQuickwire, Recipes.Wire],
)
Items.AluminumScrap._attach_recipes(
    [Recipes.AluminumScrap, Recipes.ElectrodeAluminumScrap, Recipes.InstantScrap],
    [Recipes.PureAluminumIngot, Recipes.AluminumIngot],
)
Items.AluminumCasing._attach_recipes(
    [Recipes.AluminumCasing, Recipes.AlcladCasing],
    [Recipes.Battery, Recipes.RadioControlUnit, Recipes.RadioControlSystem, Recipes.FusedModularFrame, Recipes.InstantPlutoniumCell, Recipes.HeatExchanger, Recipes.IodineInfusedFilter, Recipes.TurboRifleAmmo],
)
Items.AluminaSolution._attach_recipes(
    [Recipes.AluminaSolution, Recipes.UnpackageAluminaSolution, Recipes.SloppyAlumina],
    [Recipes.AluminumScrap, Recipes.PackagedAluminaSolution, Recipes.ElectrodeAluminumScrap, Recipes.Battery],
)
Items.Computer._attach_recipes(
    [Recipes.Computer, Recipes.CrystalComputer, Recipes.CateriumComputer],
    [Recipes.AdaptiveControlUnit, Recipes.Supercomputer, Recipes.RadioControlUnit, Recipes.SuperStateComputer, Recipes.Hoverpack],
)
Items.HeavyModularFrame._attach_recipes(
    [Recipes.HeavyFlexibleFrame, Recipes.HeavyModularFrame, Recipes.HeavyEncasedFrame],
    [Recipes.AdaptiveControlUnit, Recipes.FusedModularFrame, Recipes.HeatFusedFrame, Recipes.Hoverpack],
)
Items.SmartPlating._attach_recipes(
    [Recipes.PlasticSmartPlating, Recipes.SmartPlating],
    [Recipes.ModularEngine],
)
Items.HighSpeedConnector._attach_recipes(
    [Recipes.HighSpeedConnector, Recipes.SiliconHighSpeedConnector],
    [Recipes.AutomatedSpeedWiring, Recipes.Supercomputer, Recipes.RadioConnectionUnit, Recipes.ElectromagneticConnectionRod, Recipes.HomingRifleAmmo],
)
Items.AutomatedWiring._attach_recipes(
    [Recipes.AutomatedSpeedWiring, Recipes.AutomatedWiring],
    [Recipes.AdaptiveControlUnit],
)
Items.Stator._attach_recipes(
    [Recipes.Stator, Recipes.QuickwireStator],
    [Recipes.AutomatedSpeedWiring, Recipes.Motor, Recipes.AutomatedWiring, Recipes.TurboPressureMotor, Recipes.ElectromagneticControlRod, Recipes.RigorMotor, Recipes.ElectromagneticConnectionRod],
)
Items.AILimiter._attach_recipes(
    [Recipes.AILimiter, Recipes.PlasticAILimiter],
    [Recipes.Supercomputer, Recipes.ElectromagneticControlRod, Recipes.InsulatedCrystalOscillator, Recipes.NukeNobelisk],
)
Items.Quickwire._attach_recipes(
    [Recipes.FusedQuickwire, Recipes.Quickwire],
    [Recipes.AILimiter, Recipes.HighSpeedConnector, Recipes.PlasticAILimiter, Recipes.InfusedUraniumCell, Recipes.QuickwireStator, Recipes.SiliconHighSpeedConnector, Recipes.CateriumComputer, Recipes.CateriumCircuitBoard, Recipes.QuickwireCable, Recipes.IodineInfusedFilter, Recipes.StunRebar, Recipes.Zipline],
)
Items.ModularEngine._attach_recipes(
    [Recipes.ModularEngine],
    [Recipes.ThermalPropulsionRocket],
)
Items.AdaptiveControlUnit._attach_recipes(
    [Recipes.AdaptiveControlUnit],
    [Recipes.AssemblyDirectorSystem],
)
Items.PressureConversionCube._attach_recipes(
    [Recipes.PressureConversionCube],
    [Recipes.TurboPressureMotor, Recipes.NuclearPasta, Recipes.PlutoniumFuelUnit],
)
Items.EncasedPlutoniumCell._attach_recipes(
    [Recipes.EncasedPlutoniumCell, Recipes.InstantPlutoniumCell],
    [Recipes.PlutoniumFuelRod, Recipes.PlutoniumFuelUnit],
)
Items.PlutoniumPellet._attach_recipes(
    [Recipes.PlutoniumPellet],
    [Recipes.EncasedPlutoniumCell],
)
Items.NonFissileUranium._attach_recipes(
    [Recipes.NonFissileUranium, Recipes.FertileUranium],
    [Recipes.PlutoniumPellet, Recipes.InstantPlutoniumCell],
)
Items.SulfuricAcid._attach_recipes(
    [Recipes.EncasedUraniumCell, Recipes.SulfuricAcid, Recipes.UnpackageSulfuricAcid],
    [Recipes.NonFissileUranium, Recipes.EncasedUraniumCell, Recipes.Battery, Recipes.PackagedSulfuricAcid, Recipes.InstantScrap, Recipes.FertileUranium, Recipes.LeachedIroningot, Recipes.LeachedCopperIngot, Recipes.LeachedCateriumIngot],
)
Items.CopperPowder._attach_recipes(
    [Recipes.CopperPowder],
    [Recipes.NuclearPasta],
)
Items.HeatSink._attach_recipes(
    [Recipes.HeatSink, Recipes.HeatExchanger],
    [Recipes.PlutoniumFuelRod, Recipes.CoolingSystem, Recipes.CoolingDevice, Recipes.RadioConnectionUnit],
)
Items.ElectromagneticControlRod._attach_recipes(
    [Recipes.ElectromagneticControlRod, Recipes.ElectromagneticConnectionRod],
    [Recipes.PlutoniumFuelRod, Recipes.SuperStateComputer, Recipes.UraniumFuelRod, Recipes.MagneticFieldGenerator, Recipes.ElectricMotor, Recipes.TurboElectricMotor, Recipes.UraniumFuelUnit, Recipes.FicsoniumFuelRod],
)
Items.NuclearPasta._attach_recipes(
    [Recipes.NuclearPasta],
    [Recipes.SingularityCell],
)
Items.EncasedUraniumCell._attach_recipes(
    [Recipes.EncasedUraniumCell, Recipes.InfusedUraniumCell],
    [Recipes.UraniumFuelRod, Recipes.UraniumFuelUnit, Recipes.NukeNobelisk],
)
Items.DissolvedSilica._attach_recipes(
    [Recipes.QuartzPurification],
    [Recipes.DistilledSilica],
)
Items.ThermalPropulsionRocket._attach_recipes(
    [Recipes.ThermalPropulsionRocket],
    [Recipes.BallisticWarpDrive],
)
Items.BlackPowder._attach_recipes(
    [Recipes.FineBlackPowder, Recipes.BlackPowder],
    [Recipes.Nobelisk, Recipes.SmokelessPowder],
)
Items.Ficsonium._attach_recipes(
    [Recipes.Ficsonium],
    [Recipes.FicsoniumFuelRod],
)
Items.SingularityCell._attach_recipes(
    [Recipes.SingularityCell],
    [Recipes.Ficsonium, Recipes.BallisticWarpDrive],
)
Items.BallisticWarpDrive._attach_recipes(
    [Recipes.BallisticWarpDrive],
    [],
)
Items.GasFilter._attach_recipes(
    [Recipes.GasFilter],
    [Recipes.IodineInfusedFilter],
)
Items.AlienProtein._attach_recipes(
    [Recipes.HogProtein, Recipes.SpitterProtein, Recipes.StingerProtein, Recipes.HatcherProtein],
    [Recipes.AlienDNACapsule, Recipes.BiomassFromAlienProtein, Recipes.ProteinInhaler, Recipes.TherapeuticInhaler],
)
Items.BluePowerSlug._attach_recipes(
    [],
    [Recipes.PowerShardFrom1],
)
Items.AlienDNACapsule._attach_recipes(
    [Recipes.AlienDNACapsule],
    [],
)
Items.PurplePowerSlug._attach_recipes(
    [],
    [Recipes.PowerShardFrom5],
)
Items.YellowPowerSlug._attach_recipes(
    [],
    [Recipes.PowerShardFrom2],
)
Items.SmokelessPowder._attach_recipes(
    [Recipes.SmokelessPowder],
    [Recipes.NukeNobelisk, Recipes.RifleAmmo, Recipes.ExplosiveRebar, Recipes.ClusterNobelisk],
)
Items.RebarGun._attach_recipes(
    [Recipes.RebarGun],
    [],
)
Items.Rifle._attach_recipes(
    [Recipes.Rifle],
    [],
)
Items.UraniumFuelRod._attach_recipes(
    [Recipes.UraniumFuelRod, Recipes.UraniumFuelUnit],
    [],
)
Items.PlutoniumFuelRod._attach_recipes(
    [Recipes.PlutoniumFuelRod, Recipes.PlutoniumFuelUnit],
    [],
)
Items.FicsoniumFuelRod._attach_recipes(
    [Recipes.FicsoniumFuelRod],
    [],
)
Items.ExplosiveRebar._attach_recipes(
    [Recipes.ExplosiveRebar],
    [],
)
Items.StunRebar._attach_recipes(
    [Recipes.StunRebar],
    [],
)
Items.HomingRifleAmmo._attach_recipes(
    [Recipes.HomingRifleAmmo],
    [],
)
Items.ClusterNobelisk._attach_recipes(
    [Recipes.ClusterNobelisk],
    [],
)
Items.Nobelisk._attach_recipes(
    [Recipes.Nobelisk],
    [Recipes.GasNobelisk, Recipes.PulseNobelisk, Recipes.NukeNobelisk, Recipes.ClusterNobelisk],
)
Items.GasNobelisk._attach_recipes(
    [Recipes.GasNobelisk],
    [],
)
Items.NukeNobelisk._attach_recipes(
    [Recipes.NukeNobelisk],
    [],
)
Items.PulseNobelisk._attach_recipes(
    [Recipes.PulseNobelisk],
    [],
)
Items.IronRebar._attach_recipes(
    [Recipes.IronRebar],
    [Recipes.StunRebar, Recipes.ShatterRebar, Recipes.ExplosiveRebar],
)
Items.HazmatSuit._attach_recipes(
    [Recipes.HazmatSuit],
    [],
)
Items.NobeliskDetonator._attach_recipes(
    [Recipes.NobeliskDetonator],
    [],
)
Items.FactoryCart._attach_recipes(
    [Recipes.FactoryCart],
    [],
)
Items.GoldenFactoryCart._attach_recipes(
    [Recipes.GoldenFactoryCart],
    [],
)
Items.PortableMiner._attach_recipes(
    [Recipes.AutomatedMiner, Recipes.PortableMiner],
    [],
)
Items.XenoZapper._attach_recipes(
    [Recipes.XenoZapper],
    [Recipes.XenoBasher, Recipes.Zipline],
)
Items.ObjectScanner._attach_recipes(
    [Recipes.ObjectScanner],
    [Recipes.NobeliskDetonator],
)
Items.Hoverpack._attach_recipes(
    [Recipes.Hoverpack],
    [],
)
Items.Jetpack._attach_recipes(
    [Recipes.Jetpack],
    [],
)
Items.XenoBasher._attach_recipes(
    [Recipes.XenoBasher],
    [],
)
Items.Chainsaw._attach_recipes(
    [Recipes.Chainsaw],
    [],
)
Items.BladeRunners._attach_recipes(
    [Recipes.BladeRunners],
    [],
)
Items.Zipline._attach_recipes(
    [Recipes.Zipline],
    [],
)
Items.GasMask._attach_recipes(
    [Recipes.GasMask],
    [],
)
Items.ShatterRebar._attach_recipes(
    [Recipes.ShatterRebar],
    [],
)
Items.TurboRifleAmmo._attach_recipes(
    [Recipes.TurboRifleAmmo],
    [],
)
Items.RifleAmmo._attach_recipes(
    [Recipes.RifleAmmo],
    [Recipes.HomingRifleAmmo, Recipes.TurboRifleAmmo],
)
Items.IronOre._attach_recipes(
    [Recipes.IronOreFromLimestone],
    [Recipes.IronIngot, Recipes.CoalFromIron, Recipes.SulfurFromIron, Recipes.SteelIngot, Recipes.PureIronIngot, Recipes.CopperAlloyIngot, Recipes.CokeSteelIngot, Recipes.LeachedIroningot, Recipes.BasicIronIngot, Recipes.CompactedSteelIngot, Recipes.IronAlloyIngot],
)
Items.Coal._attach_recipes(
    [Recipes.CoalFromIron, Recipes.CoalFromLimestone, Recipes.Charcoal, Recipes.Biocoal],
    [Recipes.NitroRocketFuel, Recipes.TurboDiamonds, Recipes.Diamonds, Recipes.RawQuartzFromCoal, Recipes.SulfurFromCoal, Recipes.CompactedCoal, Recipes.PinkDiamonds, Recipes.CloudyDiamonds, Recipes.SteelIngot, Recipes.AluminumScrap, Recipes.InstantScrap, Recipes.FusedQuartzCrystal, Recipes.SolidSteelIngot, Recipes.BlackPowder, Recipes.GasFilter],
)
Items.Water._attach_recipes(
    [Recipes.UnpackageWater, Recipes.AluminumScrap, Recipes.ElectrodeAluminumScrap, Recipes.NonFissileUranium, Recipes.Battery, Recipes.InstantScrap, Recipes.FertileUranium, Recipes.DistilledSilica],
    [Recipes.BiochemicalSculptor, Recipes.ResidualPlastic, Recipes.ResidualRubber, Recipes.WetConcrete, Recipes.LiquidBiofuel, Recipes.PackagedWater, Recipes.SteamedCopperSheet, Recipes.PureQuartzCrystal, Recipes.PureIronIngot, Recipes.PureCopperIngot, Recipes.PureCateriumIngot, Recipes.AluminaSolution, Recipes.NitricAcid, Recipes.CoolingSystem, Recipes.SulfuricAcid, Recipes.SloppyAlumina, Recipes.InstantScrap, Recipes.DilutedFuel, Recipes.DistilledSilica, Recipes.PolyesterFabric],
)
Items.NitrogenGas._attach_recipes(
    [Recipes.NitrogenGasFromBauxite, Recipes.NitrogenGasFromCaterium, Recipes.UnpackageNitrogenGas],
    [Recipes.NitroRocketFuel, Recipes.NitricAcid, Recipes.CoolingSystem, Recipes.FusedModularFrame, Recipes.PackagedNitrogenGas, Recipes.CoolingDevice],
)
Items.Sulfur._attach_recipes(
    [Recipes.SulfurFromCoal, Recipes.SulfurFromIron],
    [Recipes.NitroRocketFuel, Recipes.CopperOreFromSulfur, Recipes.LimestoneFromSulfur, Recipes.CompactedCoal, Recipes.TurboBlendFuel, Recipes.SulfuricAcid, Recipes.ClassicBattery, Recipes.InfusedUraniumCell, Recipes.FineBlackPowder, Recipes.BlackPowder],
)
Items.SAM._attach_recipes(
    [],
    [Recipes.ReanimatedSAM],
)
Items.Bauxite._attach_recipes(
    [Recipes.BauxiteFromCaterium, Recipes.BauxiteFromCopper],
    [Recipes.NitrogenGasFromBauxite, Recipes.RawQuartzFromBauxite, Recipes.UraniumOreFromBauxite, Recipes.AluminaSolution, Recipes.SloppyAlumina, Recipes.InstantScrap],
)
Items.CateriumOre._attach_recipes(
    [Recipes.CateriumOreFromCopper, Recipes.CateriumOreFromQuartz],
    [Recipes.BauxiteFromCaterium, Recipes.NitrogenGasFromCaterium, Recipes.PureCateriumIngot, Recipes.TemperedCateriumIngot, Recipes.LeachedCateriumIngot, Recipes.CateriumIngot],
)
Items.CopperOre._attach_recipes(
    [Recipes.CopperOreFromQuartz, Recipes.CopperOreFromSulfur],
    [Recipes.BauxiteFromCopper, Recipes.CateriumOreFromCopper, Recipes.PureCopperIngot, Recipes.CopperAlloyIngot, Recipes.TemperedCopperIngot, Recipes.LeachedCopperIngot, Recipes.IronAlloyIngot, Recipes.CopperIngot],
)
Items.RawQuartz._attach_recipes(
    [Recipes.RawQuartzFromBauxite, Recipes.RawQuartzFromCoal],
    [Recipes.CateriumOreFromQuartz, Recipes.CopperOreFromQuartz, Recipes.PureQuartzCrystal, Recipes.QuartzCrystal, Recipes.Silica, Recipes.QuartzPurification, Recipes.FusedQuartzCrystal, Recipes.CheapSilica],
)
Items.Limestone._attach_recipes(
    [Recipes.LimestoneFromSulfur],
    [Recipes.CoalFromLimestone, Recipes.IronOreFromLimestone, Recipes.CloudyDiamonds, Recipes.WetConcrete, Recipes.RubberConcrete, Recipes.DistilledSilica, Recipes.BasicIronIngot, Recipes.CheapSilica, Recipes.FineConcrete, Recipes.Concrete],
)
Items.Uranium._attach_recipes(
    [Recipes.UraniumOreFromBauxite],
    [Recipes.EncasedUraniumCell, Recipes.FertileUranium, Recipes.InfusedUraniumCell],
)
Items.CrudeOil._attach_recipes(
    [Recipes.UnpackageOil],
    [Recipes.Fuel, Recipes.Plastic, Recipes.Rubber, Recipes.OilBasedDiamonds, Recipes.PackagedOil, Recipes.PolymerResin, Recipes.HeavyOilResidue],
)
Items.MedicinalInhaler._attach_recipes(
    [Recipes.ProteinInhaler, Recipes.TherapeuticInhaler, Recipes.VitaminInhaler, Recipes.NutritionalInhaler],
    [],
)
Items.SolidBiofuel._attach_recipes(
    [Recipes.SolidBiofuel],
    [Recipes.LiquidBiofuel],
)
Items.PackagedLiquidBiofuel._attach_recipes(
    [Recipes.PackagedLiquidBiofuel],
    [Recipes.UnpackageLiquidBiofuel],
)
Items.Biomass._attach_recipes(
    [Recipes.BiomassFromMycelia, Recipes.BiomassFromAlienProtein, Recipes.BiomassFromLeaves, Recipes.BiomassFromWood],
    [Recipes.Biocoal, Recipes.SolidBiofuel, Recipes.GasNobelisk, Recipes.Fabric],
)
Items.Leaves._attach_recipes(
    [],
    [Recipes.BiomassFromLeaves],
)
Items.Mycelia._attach_recipes(
    [],
    [Recipes.BiomassFromMycelia, Recipes.TherapeuticInhaler, Recipes.VitaminInhaler, Recipes.Fabric],
)
Items.Wood._attach_recipes(
    [],
    [Recipes.Charcoal, Recipes.BiomassFromWood],
)
Items.LiquidBiofuel._attach_recipes(
    [Recipes.LiquidBiofuel, Recipes.UnpackageLiquidBiofuel],
    [Recipes.PackagedLiquidBiofuel],
)
Items.PackagedAluminaSolution._attach_recipes(
    [Recipes.PackagedAluminaSolution],
    [Recipes.UnpackageAluminaSolution],
)
Items.PackagedNitrogenGas._attach_recipes(
    [Recipes.PackagedNitrogenGas],
    [Recipes.TurboPressureMotor, Recipes.UnpackageNitrogenGas],
)
Items.PackagedNitricAcid._attach_recipes(
    [Recipes.PackagedNitricAcid],
    [Recipes.UnpackageNitricAcid],
)
Items.PackagedSulfuricAcid._attach_recipes(
    [Recipes.PackagedSulfuricAcid],
    [Recipes.UnpackageSulfuricAcid],
)
Items.Fabric._attach_recipes(
    [Recipes.PolyesterFabric, Recipes.Fabric],
    [Recipes.HazmatSuit, Recipes.GasFilter, Recipes.GasMask, Recipes.Parachute],
)
Items.HogRemains._attach_recipes(
    [],
    [Recipes.HogProtein],
)
Items.SpitterRemains._attach_recipes(
    [],
    [Recipes.SpitterProtein],
)
Items.StingerRemains._attach_recipes(
    [],
    [Recipes.StingerProtein],
)
Items.HatcherRemains._attach_recipes(
    [],
    [Recipes.HatcherProtein],
)
Items.PowerShard._attach_recipes(
    [Recipes.PowerShardFrom1, Recipes.SyntheticPowerShard, Recipes.PowerShardFrom5, Recipes.PowerShardFrom2],
    [Recipes.IonizedFuel, Recipes.AlienPowerMatrix],
)
Items.Paleberry._attach_recipes(
    [],
    [Recipes.VitaminInhaler, Recipes.NutritionalInhaler],
)
Items.BerylNut._attach_recipes(
    [],
    [Recipes.ProteinInhaler, Recipes.NutritionalInhaler],
)
Items.BaconAgaric._attach_recipes(
    [],
    [Recipes.TherapeuticInhaler, Recipes.NutritionalInhaler],
)
Items.Parachute._attach_recipes(
    [Recipes.Parachute],
    [],
)
Items.AlienPowerMatrix._attach_recipes(
    [Recipes.AlienPowerMatrix],
    [],
)
