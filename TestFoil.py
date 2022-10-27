from knowledge import *
A, B, C, D, E, F, G, H, I, x, y, z = map(expr, 'ABCDEFGHIxyz')
# 背景性的知识放入FOILContainer中
small_family = FOILContainer([expr("Female(Ann)"),
                              expr("Female(Mary)"),
                              expr("Female(Eve)"),
                              expr("ParentOf(Ann,Mary)"),
                              expr("ParentOf(Eve,Tom)"),
                              expr("ParentOf(Bob,Mary)"),
                             ])


#目标谓词P：DaughterOf(x, y)
target = expr('DaughterOf(x, y)')

# P的正例部分：使用知识库中已有的三元组来构建
examples_pos = [{x: expr('Mary'), y: expr('Ann')},
                {x: expr('Mary'), y: expr('Bob')}]


# P的反例部分：用否定已有确定关系的三元组的方式来构建
examples_neg = [{x: expr('Tom'), y: expr('Ann')},
                {x: expr('Tom'), y: expr('Bob')},
                {x: expr('Tom'), y: expr('Eve')},
                {x: expr('Mary'), y: expr('Eve')}]
# run the FOIL algorithm 
clauses = small_family.foil([examples_pos, examples_neg], target)

# 规则头 DaughterOf(x,y)的规则体
print (clauses)
print("-"*55)


# ----------------------------------------------------------------------

small_family = FOILContainer([expr("Sibling(Ann,Mike)"),
                              expr("Couple(David,James)"),
                              expr("Mother(James,Ann)"),
                              expr("Mother(James,MIke)"),
                             ])


# 要推导的部分:目标谓词P
target = expr('Father(x, y)')

# P的正例部分：使用知识库中已有的三元组来构建
examples_pos = [{x: expr('David'), y: expr('Mike')}]


# P的反例部分：用否定已有确定关系的三元组的方式来构建
examples_neg = [{x: expr('David'), y: expr('James')},
                {x: expr('James'), y: expr('Ann')},
                {x: expr('James'), y: expr('Mike')},
                {x: expr('Ann'), y: expr('Mike')}]
# run the FOIL algorithm
clauses = small_family.foil([examples_pos, examples_neg], target)

# Father(x,y)的规则体
print (clauses)
