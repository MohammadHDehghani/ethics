import sys
from ethics.plans.semantics import Situation
from ethics.plans.principles import KantianHumanity, DoNoHarm, DoNoInstrumentalHarm, Utilitarianism, Deontology, GoalDeontology, DoubleEffectPrinciple, AvoidAnyHarm, AvoidAvoidableHarm

sit = Situation(f"./plans/{sys.argv[1]}.yaml")

perm = sit.evaluate(Deontology)
print("Deontology: ", perm)

perm = sit.evaluate(GoalDeontology)
print("GoalDeontology: ", perm)

perm = sit.evaluate(KantianHumanity)
print("Kantian: ", perm)

perm = sit.evaluate(KantianHumanity, 2)
print("Kantian Reading #2: ", perm)

perm = sit.evaluate(DoNoHarm)
print("DoNoHarm: ", perm)

perm = sit.evaluate(DoNoInstrumentalHarm)
print("DoNoInstrumentalHarm: ", perm)

perm = sit.evaluate(Utilitarianism)
print("Utilitarianism: ", perm)

perm = sit.evaluate(DoubleEffectPrinciple)
print("DoubleEffectPrinciple: ", perm)

perm = sit.evaluate(AvoidAvoidableHarm)
print("AvoidAvoidableHarm: ", perm)

perm = sit.evaluate(AvoidAnyHarm)
print("AvoidAnyHarm: ", perm)
