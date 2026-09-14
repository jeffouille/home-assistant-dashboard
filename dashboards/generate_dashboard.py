import json

config = {
    "title": "Maison 2026",
    "views": [
        # ─── VUE PRINCIPALE : REZ-DE-CHAUSSÉE ──────────────────────────────────
        {
            "title": "Rez-de-chaussée",
            "path": "rdc",
            "icon": "mdi:home-floor-0",
            "type": "sections",
            "max_columns": 3,
            "sections": [
                {
                    "title": "Vue Générale",
                    "cards": [
                        {
                            "type": "custom:button-card",
                            "entity": "weather.issy_les_moulineaux",
                            "show_name": False,
                            "show_icon": False,
                            "show_state": False,
                            "custom_fields": {
                                "weather_hero": """[[[
  const d = new Date();
  const hours = String(d.getHours()).padStart(2, '0');
  const mins = String(d.getMinutes()).padStart(2, '0');
  const days = ['Dimanche','Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi'];
  const months = ['janvier','février','mars','avril','mai','juin','juillet','août','septembre','octobre','novembre','décembre'];
  const dateStr = `${days[d.getDay()]} ${d.getDate()} ${months[d.getMonth()]}`;
  const temp = entity?.attributes?.temperature ?? '—';
  const cond = entity?.state ?? '';
  return `
    <div style="display:flex; justify-content:space-between; align-items:flex-start; width:100%;">
      <div>
        <div style="font-family:'Poppins',sans-serif; font-size:42px; font-weight:600; color:#ffffff; line-height:1.1; letter-spacing:-1px;">
          ${hours}:${mins}
        </div>
        <div style="font-family:'Poppins',sans-serif; font-size:13px; font-weight:400; color:#eac578; margin-top:4px;">
          ${dateStr}
        </div>
      </div>
      <div style="text-align:right; font-family:'Poppins',sans-serif;">
        <div style="font-size:28px; font-weight:600; color:#ffffff;">
          ${temp}°C
        </div>
        <div style="font-size:12px; color:rgba(255,255,255,0.6); text-transform:capitalize;">
          ${cond} · Issy
        </div>
      </div>
    </div>
  `;
]]]"""
                            },
                            "styles": {
                                "card": [
                                    {"background": "#1e2022"},
                                    {"border-radius": "18px"},
                                    {"border": "1px solid rgba(234, 197, 120, 0.15)"},
                                    {"box-shadow": "0 4px 20px rgba(0, 0, 0, 0.4)"},
                                    {"padding": "20px 22px"}
                                ]
                            }
                        },
                        {
                            "type": "grid",
                            "columns": 2,
                            "square": False,
                            "cards": [
                                {
                                    "type": "custom:button-card",
                                    "entity": "light.lumieres_rdc",
                                    "name": "Lumières RDC",
                                    "show_name": True,
                                    "show_icon": True,
                                    "show_state": True,
                                    "tap_action": {"action": "toggle"},
                                    "styles": {
                                        "card": [
                                            {"background": "#1e2022"},
                                            {"border-radius": "16px"},
                                            {"border": "1px solid rgba(255,255,255,0.06)"},
                                            {"padding": "14px"}
                                        ],
                                        "grid": [
                                            {"grid-template-areas": '"i n" "i s"'},
                                            {"grid-template-columns": "min-content 1fr"},
                                            {"gap": "2px 10px"},
                                            {"align-items": "center"}
                                        ],
                                        "img_cell": [
                                            {"background": "#141414"},
                                            {"border-radius": "12px"},
                                            {"width": "40px"},
                                            {"height": "40px"}
                                        ],
                                        "icon": [
                                            {"width": "24px"},
                                            {"height": "24px"},
                                            {"color": "[[[ return entity.state === 'on' ? '#eac578' : 'rgba(255,255,255,0.3)'; ]]]"}
                                        ],
                                        "name": [
                                            {"font-family": "'Poppins', sans-serif"},
                                            {"font-size": "13px"},
                                            {"font-weight": "600"},
                                            {"color": "#ffffff"},
                                            {"text-align": "left"}
                                        ],
                                        "state": [
                                            {"font-family": "'Poppins', sans-serif"},
                                            {"font-size": "11px"},
                                            {"color": "rgba(255,255,255,0.6)"},
                                            {"text-align": "left"}
                                        ]
                                    }
                                },
                                {
                                    "type": "custom:button-card",
                                    "entity": "cover.volet_porte_fenetre",
                                    "name": "Volet Salon",
                                    "show_name": True,
                                    "show_icon": True,
                                    "show_state": True,
                                    "tap_action": {"action": "more-info"},
                                    "styles": {
                                        "card": [
                                            {"background": "#1e2022"},
                                            {"border-radius": "16px"},
                                            {"border": "1px solid rgba(255,255,255,0.06)"},
                                            {"padding": "14px"}
                                        ],
                                        "grid": [
                                            {"grid-template-areas": '"i n" "i s"'},
                                            {"grid-template-columns": "min-content 1fr"},
                                            {"gap": "2px 10px"},
                                            {"align-items": "center"}
                                        ],
                                        "img_cell": [
                                            {"background": "#141414"},
                                            {"border-radius": "12px"},
                                            {"width": "40px"},
                                            {"height": "40px"}
                                        ],
                                        "icon": [
                                            {"width": "24px"},
                                            {"height": "24px"},
                                            {"color": "[[[ return entity.state === 'open' ? '#38f2e9' : 'rgba(255,255,255,0.3)'; ]]]"}
                                        ],
                                        "name": [
                                            {"font-family": "'Poppins', sans-serif"},
                                            {"font-size": "13px"},
                                            {"font-weight": "600"},
                                            {"color": "#ffffff"},
                                            {"text-align": "left"}
                                        ],
                                        "state": [
                                            {"font-family": "'Poppins', sans-serif"},
                                            {"font-size": "11px"},
                                            {"color": "rgba(255,255,255,0.6)"},
                                            {"text-align": "left"}
                                        ]
                                    }
                                },
                                {
                                    "type": "custom:button-card",
                                    "entity": "media_player.marantz_nr1607",
                                    "name": "Marantz",
                                    "show_name": True,
                                    "show_icon": True,
                                    "show_state": True,
                                    "tap_action": {"action": "more-info"},
                                    "styles": {
                                        "card": [
                                            {"background": "#1e2022"},
                                            {"border-radius": "16px"},
                                            {"border": "1px solid rgba(255,255,255,0.06)"},
                                            {"padding": "14px"}
                                        ],
                                        "grid": [
                                            {"grid-template-areas": '"i n" "i s"'},
                                            {"grid-template-columns": "min-content 1fr"},
                                            {"gap": "2px 10px"},
                                            {"align-items": "center"}
                                        ],
                                        "img_cell": [
                                            {"background": "#141414"},
                                            {"border-radius": "12px"},
                                            {"width": "40px"},
                                            {"height": "40px"}
                                        ],
                                        "icon": [
                                            {"width": "24px"},
                                            {"height": "24px"},
                                            {"color": "[[[ return (entity.state === 'on' || entity.state === 'playing') ? '#eac578' : 'rgba(255,255,255,0.3)'; ]]]"}
                                        ],
                                        "name": [
                                            {"font-family": "'Poppins', sans-serif"},
                                            {"font-size": "13px"},
                                            {"font-weight": "600"},
                                            {"color": "#ffffff"},
                                            {"text-align": "left"}
                                        ],
                                        "state": [
                                            {"font-family": "'Poppins', sans-serif"},
                                            {"font-size": "11px"},
                                            {"color": "rgba(255,255,255,0.6)"},
                                            {"text-align": "left"}
                                        ]
                                    }
                                },
                                {
                                    "type": "custom:button-card",
                                    "entity": "climate.versatile_thermostat_global_salon",
                                    "name": "Thermostat",
                                    "show_name": True,
                                    "show_icon": True,
                                    "show_state": True,
                                    "tap_action": {"action": "more-info"},
                                    "styles": {
                                        "card": [
                                            {"background": "#1e2022"},
                                            {"border-radius": "16px"},
                                            {"border": "1px solid rgba(255,255,255,0.06)"},
                                            {"padding": "14px"}
                                        ],
                                        "grid": [
                                            {"grid-template-areas": '"i n" "i s"'},
                                            {"grid-template-columns": "min-content 1fr"},
                                            {"gap": "2px 10px"},
                                            {"align-items": "center"}
                                        ],
                                        "img_cell": [
                                            {"background": "#141414"},
                                            {"border-radius": "12px"},
                                            {"width": "40px"},
                                            {"height": "40px"}
                                        ],
                                        "icon": [
                                            {"width": "24px"},
                                            {"height": "24px"},
                                            {"color": "[[[ return entity.state === 'heat' ? '#eac578' : 'rgba(255,255,255,0.3)'; ]]]"}
                                        ],
                                        "name": [
                                            {"font-family": "'Poppins', sans-serif"},
                                            {"font-size": "13px"},
                                            {"font-weight": "600"},
                                            {"color": "#ffffff"},
                                            {"text-align": "left"}
                                        ],
                                        "state": [
                                            {"font-family": "'Poppins', sans-serif"},
                                            {"font-size": "11px"},
                                            {"color": "rgba(255,255,255,0.6)"},
                                            {"text-align": "left"}
                                        ]
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Espaces de Vie",
                    "cards": [
                        # Carte Pièce : Salon
                        {
                            "type": "custom:button-card",
                            "name": "Salon",
                            "icon": "mdi:sofa",
                            "entity": "binary_sensor.presence_salon_occupancy",
                            "tap_action": {
                                "action": "navigate",
                                "navigation_path": "/dashboard-maison-2026/salon"
                            },
                            "custom_fields": {
                                "room_info": """[[[
  const temp = states['sensor.alpstuga_air_quality_monitor_temperature']?.state ?? '—';
  const hum = states['sensor.alpstuga_air_quality_monitor_humidite']?.state ?? '—';
  const presence = entity?.state === 'on' ? 'Présence détectée' : 'Inoccupé';
  const pColor = entity?.state === 'on' ? '#38f2e9' : 'rgba(255,255,255,0.5)';
  return `
    <div style="display:flex; justify-content:space-between; align-items:center; width:100%; font-family:'Poppins',sans-serif;">
      <div>
        <div style="font-size:20px; font-weight:600; color:#ffffff; line-height:1.2;">Salon</div>
        <div style="font-size:12px; color:${pColor}; margin-top:2px;">${presence}</div>
      </div>
      <div style="text-align:right;">
        <div style="font-size:22px; font-weight:600; color:#eac578;">${temp}°C</div>
        <div style="font-size:11px; color:rgba(255,255,255,0.5);">${hum}% hum.</div>
      </div>
    </div>
  `;
]]]"""
                            },
                            "styles": {
                                "card": [
                                    {"background": "#1e2022"},
                                    {"border-radius": "18px"},
                                    {"border": "1px solid rgba(255,255,255,0.06)"},
                                    {"box-shadow": "0 4px 16px rgba(0,0,0,0.3)"},
                                    {"padding": "18px 20px"}
                                ],
                                "grid": [
                                    {"grid-template-areas": '"i room_info"'},
                                    {"grid-template-columns": "min-content 1fr"},
                                    {"gap": "8px 14px"},
                                    {"align-items": "center"}
                                ],
                                "img_cell": [
                                    {"background": "#141414"},
                                    {"border-radius": "14px"},
                                    {"width": "44px"},
                                    {"height": "44px"}
                                ],
                                "icon": [
                                    {"width": "26px"},
                                    {"height": "26px"},
                                    {"color": "#eac578"}
                                ],
                                "custom_fields": {
                                    "room_info": [{"width": "100%"}]
                                }
                            }
                        },
                        # Carte Pièce : Cuisine
                        {
                            "type": "custom:button-card",
                            "name": "Cuisine",
                            "icon": "mdi:countertop",
                            "entity": "sensor.temperature_humidite_cuisine_temperature",
                            "tap_action": {
                                "action": "navigate",
                                "navigation_path": "/dashboard-maison-2026/cuisine"
                            },
                            "custom_fields": {
                                "room_info": """[[[
  const temp = entity?.state ?? '—';
  const hum = states['sensor.temperature_humidite_cuisine_humidity']?.state ?? '—';
  const fenetre = states['binary_sensor.fenetre_cuisine_contact']?.state === 'on' ? 'Fenêtre ouverte' : 'Fermée';
  const fColor = states['binary_sensor.fenetre_cuisine_contact']?.state === 'on' ? '#eac578' : 'rgba(255,255,255,0.5)';
  return `
    <div style="display:flex; justify-content:space-between; align-items:center; width:100%; font-family:'Poppins',sans-serif;">
      <div>
        <div style="font-size:20px; font-weight:600; color:#ffffff; line-height:1.2;">Cuisine</div>
        <div style="font-size:12px; color:${fColor}; margin-top:2px;">${fenetre}</div>
      </div>
      <div style="text-align:right;">
        <div style="font-size:22px; font-weight:600; color:#eac578;">${temp}°C</div>
        <div style="font-size:11px; color:rgba(255,255,255,0.5);">${hum}% hum.</div>
      </div>
    </div>
  `;
]]]"""
                            },
                            "styles": {
                                "card": [
                                    {"background": "#1e2022"},
                                    {"border-radius": "18px"},
                                    {"border": "1px solid rgba(255,255,255,0.06)"},
                                    {"box-shadow": "0 4px 16px rgba(0,0,0,0.3)"},
                                    {"padding": "18px 20px"}
                                ],
                                "grid": [
                                    {"grid-template-areas": '"i room_info"'},
                                    {"grid-template-columns": "min-content 1fr"},
                                    {"gap": "8px 14px"},
                                    {"align-items": "center"}
                                ],
                                "img_cell": [
                                    {"background": "#141414"},
                                    {"border-radius": "14px"},
                                    {"width": "44px"},
                                    {"height": "44px"}
                                ],
                                "icon": [
                                    {"width": "26px"},
                                    {"height": "26px"},
                                    {"color": "#eac578"}
                                ],
                                "custom_fields": {
                                    "room_info": [{"width": "100%"}]
                                }
                            }
                        },
                        # Carte Pièce : Salle à manger
                        {
                            "type": "custom:button-card",
                            "name": "Salle à manger",
                            "icon": "mdi:table-furniture",
                            "entity": "light.lampes",
                            "tap_action": {
                                "action": "navigate",
                                "navigation_path": "/dashboard-maison-2026/salle-a-manger"
                            },
                            "custom_fields": {
                                "room_info": """[[[
  const lampState = entity?.state === 'on' ? 'Éclairage allumé' : 'Éclairage éteint';
  const lColor = entity?.state === 'on' ? '#eac578' : 'rgba(255,255,255,0.5)';
  const clim = states['climate.versatile_thermostat_salle_a_manger']?.attributes?.current_temperature ?? '—';
  return `
    <div style="display:flex; justify-content:space-between; align-items:center; width:100%; font-family:'Poppins',sans-serif;">
      <div>
        <div style="font-size:20px; font-weight:600; color:#ffffff; line-height:1.2;">Salle à manger</div>
        <div style="font-size:12px; color:${lColor}; margin-top:2px;">${lampState}</div>
      </div>
      <div style="text-align:right;">
        <div style="font-size:22px; font-weight:600; color:#eac578;">${clim}°C</div>
        <div style="font-size:11px; color:rgba(255,255,255,0.5);">Thermostat</div>
      </div>
    </div>
  `;
]]]"""
                            },
                            "styles": {
                                "card": [
                                    {"background": "#1e2022"},
                                    {"border-radius": "18px"},
                                    {"border": "1px solid rgba(255,255,255,0.06)"},
                                    {"box-shadow": "0 4px 16px rgba(0,0,0,0.3)"},
                                    {"padding": "18px 20px"}
                                ],
                                "grid": [
                                    {"grid-template-areas": '"i room_info"'},
                                    {"grid-template-columns": "min-content 1fr"},
                                    {"gap": "8px 14px"},
                                    {"align-items": "center"}
                                ],
                                "img_cell": [
                                    {"background": "#141414"},
                                    {"border-radius": "14px"},
                                    {"width": "44px"},
                                    {"height": "44px"}
                                ],
                                "icon": [
                                    {"width": "26px"},
                                    {"height": "26px"},
                                    {"color": "#eac578"}
                                ],
                                "custom_fields": {
                                    "room_info": [{"width": "100%"}]
                                }
                            }
                        }
                    ]
                },
                {
                    "title": "Entrée & Espace Nuit",
                    "cards": [
                        # Carte Pièce : Entrée
                        {
                            "type": "custom:button-card",
                            "name": "Entrée",
                            "icon": "mdi:door",
                            "entity": "binary_sensor.porte_entree_contact",
                            "tap_action": {
                                "action": "navigate",
                                "navigation_path": "/dashboard-maison-2026/entree"
                            },
                            "custom_fields": {
                                "room_info": """[[[
  const porte = entity?.state === 'on' ? 'Porte ouverte' : 'Porte fermée';
  const pColor = entity?.state === 'on' ? '#eac578' : 'rgba(255,255,255,0.5)';
  const temp = states['sensor.porte_entree_temperature']?.state ?? '—';
  return `
    <div style="display:flex; justify-content:space-between; align-items:center; width:100%; font-family:'Poppins',sans-serif;">
      <div>
        <div style="font-size:20px; font-weight:600; color:#ffffff; line-height:1.2;">Entrée</div>
        <div style="font-size:12px; color:${pColor}; margin-top:2px;">${porte}</div>
      </div>
      <div style="text-align:right;">
        <div style="font-size:22px; font-weight:600; color:#eac578;">${temp}°C</div>
        <div style="font-size:11px; color:rgba(255,255,255,0.5);">Capteur entrée</div>
      </div>
    </div>
  `;
]]]"""
                            },
                            "styles": {
                                "card": [
                                    {"background": "#1e2022"},
                                    {"border-radius": "18px"},
                                    {"border": "1px solid rgba(255,255,255,0.06)"},
                                    {"box-shadow": "0 4px 16px rgba(0,0,0,0.3)"},
                                    {"padding": "18px 20px"}
                                ],
                                "grid": [
                                    {"grid-template-areas": '"i room_info"'},
                                    {"grid-template-columns": "min-content 1fr"},
                                    {"gap": "8px 14px"},
                                    {"align-items": "center"}
                                ],
                                "img_cell": [
                                    {"background": "#141414"},
                                    {"border-radius": "14px"},
                                    {"width": "44px"},
                                    {"height": "44px"}
                                ],
                                "icon": [
                                    {"width": "26px"},
                                    {"height": "26px"},
                                    {"color": "#eac578"}
                                ],
                                "custom_fields": {
                                    "room_info": [{"width": "100%"}]
                                }
                            }
                        },
                        # Carte Pièce : Chambre Filles
                        {
                            "type": "custom:button-card",
                            "name": "Chambre Filles",
                            "icon": "mdi:bed",
                            "entity": "sensor.temperature_humidite_chambre_filles_temperature",
                            "tap_action": {
                                "action": "navigate",
                                "navigation_path": "/dashboard-maison-2026/chambre-filles"
                            },
                            "custom_fields": {
                                "room_info": """[[[
  const temp = entity?.state ?? '—';
  const hum = states['sensor.temperature_humidite_chambre_filles_humidity']?.state ?? '—';
  const fenetre = states['binary_sensor.fenetre_chambre_filles_contact']?.state === 'on' ? 'Fenêtre ouverte' : 'Fermée';
  const fColor = states['binary_sensor.fenetre_chambre_filles_contact']?.state === 'on' ? '#eac578' : 'rgba(255,255,255,0.5)';
  return `
    <div style="display:flex; justify-content:space-between; align-items:center; width:100%; font-family:'Poppins',sans-serif;">
      <div>
        <div style="font-size:20px; font-weight:600; color:#ffffff; line-height:1.2;">Chambre Filles</div>
        <div style="font-size:12px; color:${fColor}; margin-top:2px;">${fenetre}</div>
      </div>
      <div style="text-align:right;">
        <div style="font-size:22px; font-weight:600; color:#eac578;">${temp}°C</div>
        <div style="font-size:11px; color:rgba(255,255,255,0.5);">${hum}% hum.</div>
      </div>
    </div>
  `;
]]]"""
                            },
                            "styles": {
                                "card": [
                                    {"background": "#1e2022"},
                                    {"border-radius": "18px"},
                                    {"border": "1px solid rgba(255,255,255,0.06)"},
                                    {"box-shadow": "0 4px 16px rgba(0,0,0,0.3)"},
                                    {"padding": "18px 20px"}
                                ],
                                "grid": [
                                    {"grid-template-areas": '"i room_info"'},
                                    {"grid-template-columns": "min-content 1fr"},
                                    {"gap": "8px 14px"},
                                    {"align-items": "center"}
                                ],
                                "img_cell": [
                                    {"background": "#141414"},
                                    {"border-radius": "14px"},
                                    {"width": "44px"},
                                    {"height": "44px"}
                                ],
                                "icon": [
                                    {"width": "26px"},
                                    {"height": "26px"},
                                    {"color": "#eac578"}
                                ],
                                "custom_fields": {
                                    "room_info": [{"width": "100%"}]
                                }
                            }
                        }
                    ]
                }
            ]
        },
        # ─── SOUS-VUE 1 : SALON ──────────────────────────────────────────────
        {
            "title": "Salon",
            "path": "salon",
            "subview": True,
            "type": "sections",
            "max_columns": 2,
            "sections": [
                {
                    "title": "Confort & Ambiance",
                    "cards": [
                        {
                            "type": "tile",
                            "entity": "climate.versatile_thermostat_global_salon",
                            "name": "Chauffage Salon",
                            "icon": "mdi:thermostat",
                            "features": [
                                {"type": "target-temperature"},
                                {
                                    "type": "climate-hvac-modes",
                                    "hvac_modes": ["off", "heat"]
                                }
                            ]
                        },
                        {
                            "type": "tile",
                            "entity": "cover.volet_porte_fenetre",
                            "name": "Volet Porte-Fenêtre",
                            "icon": "mdi:window-shutter",
                            "features": [
                                {"type": "cover-open-close"}
                            ]
                        },
                        {
                            "type": "tile",
                            "entity": "media_player.marantz_nr1607",
                            "name": "Marantz Salon",
                            "icon": "mdi:speaker",
                            "features": [
                                {"type": "media-player-volume-slider"}
                            ]
                        },
                        {
                            "type": "entities",
                            "title": "Capteurs & Environnement",
                            "entities": [
                                {"entity": "sensor.alpstuga_air_quality_monitor_temperature", "name": "Température"},
                                {"entity": "sensor.alpstuga_air_quality_monitor_humidite", "name": "Humidité"},
                                {"entity": "binary_sensor.porte_fenetre_salon_contact", "name": "Porte-Fenêtre"},
                                {"entity": "binary_sensor.presence_salon_occupancy", "name": "Détection Présence"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Éclairages du Salon",
                    "cards": [
                        {
                            "type": "tile",
                            "entity": "light.ikea_salon",
                            "name": "Ambiance KAJPLATS (Groupe)",
                            "icon": "mdi:lightbulb-group",
                            "features": [
                                {"type": "light-brightness"}
                            ]
                        },
                        {
                            "type": "grid",
                            "columns": 2,
                            "square": False,
                            "cards": [
                                {"type": "tile", "entity": "light.spots_salon", "name": "Spots Salon"},
                                {"type": "tile", "entity": "light.lampe_bonhomme", "name": "Lampe Bonhomme"},
                                {"type": "tile", "entity": "light.lampe_design_plexi", "name": "Design Plexi"},
                                {"type": "tile", "entity": "light.wled_dune_weaver_pro", "name": "WLED Dune Weaver"}
                            ]
                        },
                        {
                            "type": "entities",
                            "title": "Détail Lampes KAJPLATS",
                            "entities": [
                                {"entity": "light.salon_bureau_kajplats", "name": "Bureau"},
                                {"entity": "light.salon_lampe_bibliotheque_kajplats", "name": "Bibliothèque"},
                                {"entity": "light.salon_lampe_etagere_droite_kajplats", "name": "Étagère Droite"},
                                {"entity": "light.salon_lampe_etagere_gauche_kajplats", "name": "Étagère Gauche"}
                            ]
                        }
                    ]
                }
            ]
        },
        # ─── SOUS-VUE 2 : CUISINE ────────────────────────────────────────────
        {
            "title": "Cuisine",
            "path": "cuisine",
            "subview": True,
            "type": "sections",
            "max_columns": 2,
            "sections": [
                {
                    "title": "Confort & Sécurité",
                    "cards": [
                        {
                            "type": "tile",
                            "entity": "climate.versatile_thermostat_cuisine",
                            "name": "Chauffage Cuisine",
                            "features": [
                                {"type": "target-temperature"},
                                {
                                    "type": "climate-hvac-modes",
                                    "hvac_modes": ["off", "heat"]
                                }
                            ]
                        },
                        {
                            "type": "entities",
                            "title": "État & Environnement",
                            "entities": [
                                {"entity": "sensor.temperature_humidite_cuisine_temperature", "name": "Température"},
                                {"entity": "sensor.temperature_humidite_cuisine_humidity", "name": "Humidité"},
                                {"entity": "binary_sensor.fenetre_cuisine_contact", "name": "Contact Fenêtre"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Éclairages Cuisine",
                    "cards": [
                        {"type": "tile", "entity": "light.spots_cuisine", "name": "Spots Cuisine"},
                        {"type": "tile", "entity": "light.leds_cuisine_2", "name": "Spots Plan de Travail"},
                        {"type": "tile", "entity": "light.leds_cuisine_5", "name": "Leds & Suspension Bar"}
                    ]
                }
            ]
        },
        # ─── SOUS-VUE 3 : SALLE À MANGER ─────────────────────────────────────
        {
            "title": "Salle à manger",
            "path": "salle-a-manger",
            "subview": True,
            "type": "sections",
            "max_columns": 2,
            "sections": [
                {
                    "title": "Chauffage",
                    "cards": [
                        {
                            "type": "tile",
                            "entity": "climate.versatile_thermostat_salle_a_manger",
                            "name": "Chauffage Salle à Manger",
                            "features": [
                                {"type": "target-temperature"},
                                {
                                    "type": "climate-hvac-modes",
                                    "hvac_modes": ["off", "heat"]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "Éclairages",
                    "cards": [
                        {
                            "type": "tile",
                            "entity": "light.lampes",
                            "name": "Lampes Salle à Manger",
                            "icon": "mdi:ceiling-light"
                        }
                    ]
                }
            ]
        },
        # ─── SOUS-VUE 4 : ENTRÉE ─────────────────────────────────────────────
        {
            "title": "Entrée",
            "path": "entree",
            "subview": True,
            "type": "sections",
            "max_columns": 2,
            "sections": [
                {
                    "title": "Sécurité & Chauffage",
                    "cards": [
                        {
                            "type": "tile",
                            "entity": "binary_sensor.porte_entree_contact",
                            "name": "Porte d'Entrée",
                            "icon": "mdi:door"
                        },
                        {
                            "type": "tile",
                            "entity": "climate.versatile_thermostat_entree",
                            "name": "Chauffage Entrée",
                            "features": [
                                {"type": "target-temperature"},
                                {
                                    "type": "climate-hvac-modes",
                                    "hvac_modes": ["off", "heat"]
                                }
                            ]
                        },
                        {
                            "type": "entities",
                            "title": "Capteurs",
                            "entities": [
                                {"entity": "sensor.porte_entree_temperature", "name": "Température Porte"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Éclairage",
                    "cards": [
                        {
                            "type": "tile",
                            "entity": "light.lumiere_entree",
                            "name": "Lumière Entrée",
                            "icon": "mdi:lightbulb"
                        }
                    ]
                }
            ]
        },
        # ─── SOUS-VUE 5 : CHAMBRE FILLES ─────────────────────────────────────
        {
            "title": "Chambre Filles",
            "path": "chambre-filles",
            "subview": True,
            "type": "sections",
            "max_columns": 2,
            "sections": [
                {
                    "title": "Confort & Climat",
                    "cards": [
                        {
                            "type": "tile",
                            "entity": "climate.versatile_chambre_filles",
                            "name": "Chauffage Chambre Filles",
                            "features": [
                                {"type": "target-temperature"},
                                {
                                    "type": "climate-hvac-modes",
                                    "hvac_modes": ["off", "heat"]
                                }
                            ]
                        },
                        {
                            "type": "entities",
                            "title": "Environnement & Fenêtre",
                            "entities": [
                                {"entity": "sensor.temperature_humidite_chambre_filles_temperature", "name": "Température"},
                                {"entity": "sensor.temperature_humidite_chambre_filles_humidity", "name": "Humidité"},
                                {"entity": "binary_sensor.fenetre_chambre_filles_contact", "name": "Fenêtre"}
                            ]
                        }
                    ]
                },
                {
                    "title": "Éclairages",
                    "cards": [
                        {"type": "tile", "entity": "light.lumiere_plafond_chambre_filles", "name": "Plafond Chambre Filles"},
                        {"type": "tile", "entity": "light.spots_bureau_chambre_filles", "name": "Spots Bureau"}
                    ]
                }
            ]
        }
    ]
}

with open("dashboard_maison_2026.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

print("Generated dashboard_maison_2026.json successfully with", len(config["views"]), "views.")
