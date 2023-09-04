import rules


@rules.Predicate
def is_administrator_team_member(user):
    return user.groups.filter(name="Administradores")


@rules.Predicate
def is_administrator_team_member(user):
    return user.groups.filter(name="Gerentes de ventas")


@rules.Predicate
def is_administrator_team_member(user):
    return user.groups.filter(name="Vendedores")

