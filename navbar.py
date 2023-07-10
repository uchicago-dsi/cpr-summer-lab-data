import dash_bootstrap_components as dbc
def Navbar():
    navbar = dbc.NavbarSimple(
        #children=[
            dbc.NavItem([dbc.NavLink("Fresno", href="/fresno"),
                        dbc.NavLink("Kern", href="/kern"),
                        dbc.NavLink("Monterey", href="/monterey"),
                        dbc.NavLink("Los Angeles", href="/los-angeles"),
                        dbc.NavLink("Mendocino", href="/mendocino")]
                        ),
            # dbc.DropdownMenu(
            #     nav=True,
            #     in_navbar=True,
            #     label="Menu",
            #     children=[
            #         dbc.DropdownMenuItem("Entry 1"),
            #         dbc.DropdownMenuItem("Entry 2"),
            #         dbc.DropdownMenuItem(divider=True),
            #         dbc.DropdownMenuItem("Entry 3"),
                # ],
            # ),
        #],
    brand="Home",
    brand_href="/home",
    sticky="top",
    )
    return navbar