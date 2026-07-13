"""
colores_equipos.py
Colores oficiales de camiseta por equipo.
Cubre: selecciones de Mundial, LaLiga, Premier League, Serie A, 
       Bundesliga, Ligue 1, Eredivisie y Champions League históricos.
Si el equipo no está, devuelve un color default.
"""

COLORES = {

    # ══════════════════════════════════════════
    # SELECCIONES — MUNDIAL
    # ══════════════════════════════════════════
    "Argentina":            "#75AADB",
    "Brazil":               "#FFD700",
    "France":               "#003087",
    "Germany":              "#FFFFFF",
    "Spain":                "#C60B1E",
    "England":              "#FFFFFF",
    "Italy":                "#003399",
    "Netherlands":          "#FF6600",
    "Portugal":             "#006600",
    "Uruguay":              "#5EB6E4",
    "Croatia":              "#FF0000",
    "Belgium":              "#ED2939",
    "Mexico":               "#006847",
    "United States":        "#002868",
    "Japan":                "#003087",
    "South Korea":          "#003478",
    "Australia":            "#FFD700",
    "Morocco":              "#C1272D",
    "Senegal":              "#00853F",
    "Ghana":                "#006B3F",
    "Nigeria":              "#008751",
    "Cameroon":             "#007A5E",
    "Saudi Arabia":         "#006C35",
    "Iran":                 "#239F40",
    "Poland":               "#DC143C",
    "Switzerland":          "#FF0000",
    "Denmark":              "#C60C30",
    "Serbia":               "#C6363C",
    "Ecuador":              "#FFD100",
    "Cameroon":             "#007A5E",
    "Tunisia":              "#E70013",
    "Costa Rica":           "#002B7F",
    "Panama":               "#005293",
    "Wales":                "#C8102E",
    "Czech Republic":       "#D7141A",
    "Sweden":               "#006AA7",
    "Chile":                "#D52B1E",
    "Colombia":             "#FCD116",
    "Peru":                 "#D91023",
    "Paraguay":             "#D52B1E",
    "Bolivia":              "#007A3D",
    "Venezuela":            "#CF142B",
    "Ecuador":              "#FFD100",
    "Algeria":              "#006233",
    "Egypt":                "#C8102E",
    "Ivory Coast":          "#F77F00",
    "Russia":               "#003087",
    "Turkey":               "#E30A17",
    "Ukraine":              "#005BBB",
    "Austria":              "#ED2939",
    "Hungary":              "#436F4D",
    "Romania":              "#002B7F",
    "Slovakia":             "#003DA5",
    "Scotland":             "#003380",
    "Northern Ireland":     "#003380",
    "Republic of Ireland":  "#169B62",
    "Greece":               "#0D5EAF",
    "Slovenia":             "#003DA5",
    "Albania":              "#E41E20",
    "Finland":              "#003580",
    "Iceland":              "#003897",
    "Norway":               "#EF2B2D",
    "New Zealand":          "#000000",
    "Canada":               "#FF0000",
    "Jamaica":              "#000000",
    "Honduras":             "#0073CF",
    "El Salvador":          "#0F47AF",
    "Trinidad and Tobago":  "#CE1126",
    "Cameroon":             "#007A5E",
    "Qatar":                "#8D1B3D",

    # ══════════════════════════════════════════
    # LALIGA — ESPAÑA
    # ══════════════════════════════════════════
    "Barcelona":            "#A50044",
    "Real Madrid":          "#FFFFFF",
    "Atletico Madrid":      "#CB3524",
    "Sevilla":              "#D4AF37",
    "Valencia":             "#FF7F00",
    "Villarreal":           "#FFD700",
    "Athletic Club":        "#EE2523",
    "Real Sociedad":        "#00529F",
    "Real Betis":           "#00954C",
    "Osasuna":              "#D81E05",
    "Celta Vigo":           "#6ABDE6",
    "Getafe":               "#005999",
    "Rayo Vallecano":       "#CC0000",
    "Girona":               "#CD1625",
    "Las Palmas":           "#FFD700",
    "Alaves":               "#1B3F8B",
    "Mallorca":             "#CC0000",
    "Cadiz":                "#FFD700",
    "Almeria":              "#CC0000",
    "Espanyol":             "#004A98",
    "Levante":              "#CC0000",
    "Granada":              "#CC0000",
    "Leganes":              "#003DA5",
    "Valladolid":           "#7B1FA2",
    "Eibar":                "#003580",
    "Huesca":               "#003DA5",
    "Elche":                "#007A33",

    # ══════════════════════════════════════════
    # PREMIER LEAGUE — INGLATERRA
    # ══════════════════════════════════════════
    "Manchester City":      "#6CABDD",
    "Manchester United":    "#DA020E",
    "Liverpool":            "#C8102E",
    "Chelsea":              "#034694",
    "Arsenal":              "#EF0107",
    "Tottenham Hotspur":    "#132257",
    "Newcastle United":     "#241F20",
    "Aston Villa":          "#95BFE5",
    "West Ham United":      "#7A263A",
    "Brighton":             "#0057B8",
    "Brentford":            "#E30613",
    "Fulham":               "#000000",
    "Crystal Palace":       "#1B458F",
    "Wolverhampton":        "#FDB913",
    "Everton":              "#003399",
    "Leicester City":       "#003090",
    "Nottingham Forest":    "#DD0000",
    "Burnley":              "#6C1D45",
    "Luton Town":           "#F78F1E",
    "Sheffield United":     "#EE2737",
    "Southampton":          "#D71920",
    "Leeds United":         "#FFCD00",
    "Watford":              "#FBEE23",
    "Norwich City":         "#00A650",
    "Bournemouth":          "#DA291C",
    "Sunderland":           "#EB172B",
    "Stoke City":           "#E03A3E",
    "Swansea City":         "#121212",
    "Ipswich Town":         "#003087",

    # ══════════════════════════════════════════
    # SERIE A — ITALIA
    # ══════════════════════════════════════════
    "Juventus":             "#000000",
    "Inter":                "#010E80",
    "AC Milan":             "#FB090B",
    "Napoli":               "#12A0C7",
    "Roma":                 "#9B1A22",
    "Lazio":                "#87D8F7",
    "Atalanta":             "#1E3D8F",
    "Fiorentina":           "#4B0082",
    "Torino":               "#8B1A1A",
    "Bologna":              "#003DA5",
    "Udinese":              "#000000",
    "Sassuolo":             "#008C45",
    "Empoli":               "#1B50A0",
    "Monza":                "#ED1C24",
    "Lecce":                "#FFCC00",
    "Frosinone":            "#FFD700",
    "Genoa":                "#C8102E",
    "Cagliari":             "#C8102E",
    "Hellas Verona":        "#FFD700",
    "Venezia":              "#1B3A6B",
    "Salernitana":          "#8B0000",
    "Spezia":               "#FFFFFF",
    "Sampdoria":            "#003087",
    "Parma":                "#FFD700",

    # ══════════════════════════════════════════
    # BUNDESLIGA — ALEMANIA
    # ══════════════════════════════════════════
    "Bayern Munich":        "#DC052D",
    "Borussia Dortmund":    "#FDE100",
    "RB Leipzig":           "#DD0741",
    "Bayer Leverkusen":     "#E32221",
    "Eintracht Frankfurt":  "#E1000F",
    "Borussia Mönchengladbach": "#000000",
    "Wolfsburg":            "#65B32E",
    "Hoffenheim":           "#1457A8",
    "Freiburg":             "#CC0000",
    "Union Berlin":         "#EB1923",
    "Mainz":                "#C3001C",
    "Augsburg":             "#BA3733",
    "Werder Bremen":        "#1D9052",
    "Stuttgart":            "#E32219",
    "Köln":                 "#FF2000",
    "Hertha Berlin":        "#005CA9",
    "Schalke":              "#004D9D",
    "Hamburger SV":         "#005CA9",

    # ══════════════════════════════════════════
    # LIGUE 1 — FRANCIA
    # ══════════════════════════════════════════
    "Paris Saint-Germain":  "#004170",
    "Olympique de Marseille": "#009AC7",
    "Olympique Lyonnais":   "#003DA5",
    "Monaco":               "#D4021D",
    "Lille":                "#D9111A",
    "Rennes":               "#000000",
    "Nice":                 "#C8102E",
    "Lens":                 "#FFD700",
    "Strasbourg":           "#003DA5",
    "Montpellier":          "#F7941D",
    "Nantes":               "#FFD700",
    "Toulouse":             "#5B2D8E",
    "Brest":                "#E30613",
    "Reims":                "#C8102E",
    "Lorient":              "#F7941D",
    "Metz":                 "#8B1A1A",
    "Auxerre":              "#003DA5",
    "Angers":               "#000000",
    "Bordeaux":             "#003DA5",
    "Saint-Etienne":        "#007A33",

    # ══════════════════════════════════════════
    # EREDIVISIE — HOLANDA
    # ══════════════════════════════════════════
    "Ajax":                 "#CC0000",
    "PSV Eindhoven":        "#CC0000",
    "Feyenoord":            "#CC0000",
    "AZ Alkmaar":           "#CC0000",
    "Utrecht":              "#CC0000",
    "Twente":               "#CC0000",
    "Vitesse":              "#FFDD00",
    "Groningen":            "#009036",

    # ══════════════════════════════════════════
    # CHAMPIONS LEAGUE — HISTÓRICOS EXTRA
    # ══════════════════════════════════════════
    "Porto":                "#003DA5",
    "Benfica":              "#CC0000",
    "Sporting CP":          "#008000",
    "Celtic":               "#16A129",
    "Rangers":              "#003380",
    "Anderlecht":           "#6B1F7C",
    "Club Brugge":          "#1A5276",
    "Red Bull Salzburg":    "#DD0741",
    "Shakhtar Donetsk":     "#F7941D",
    "Dynamo Kyiv":          "#003DA5",
    "CSKA Moscow":          "#CC0000",
    "Zenit":                "#005BBB",
    "Besiktas":             "#000000",
    "Galatasaray":          "#CC0000",
    "Fenerbahce":           "#FFD700",
    "Olympiakos":           "#CC0000",
    "Panathinaikos":        "#007A33",
    "Steaua Bucharest":     "#CC0000",
    "Rosenborg":            "#000000",
    "Malmö FF":             "#005CA9",
    "Internazionale":       "#010E80",  # alias
    "Milan":                "#FB090B",  # alias
}

COLOR_DEFAULT = "#888888"

def get_color(equipo):
    """
    Devuelve el color hex del equipo.
    Busca coincidencia exacta primero, luego parcial.
    Si no encuentra nada, devuelve COLOR_DEFAULT.
    """
    if equipo in COLORES:
        return COLORES[equipo]
    # Búsqueda parcial (ej: "Borussia Dortmund CF" → "Borussia Dortmund")
    for nombre, color in COLORES.items():
        if nombre.lower() in equipo.lower() or equipo.lower() in nombre.lower():
            return color
    return COLOR_DEFAULT
