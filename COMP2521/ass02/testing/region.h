///
/// Created by Jennifer 30/01/19
///

#include <assert.h>
#include <string.h>

typedef size_t region_t;

/** Region */
enum region {
    REGION_1,
    REGION_2,
    REGION_3,
    REGION_4
};
enum { NUM_REGIONS = 4 };

///
// Places
typedef enum location {
    ADRIATIC_SEA,
    ALICANTE,
    AMSTERDAM,
    ATHENS,
    ATLANTIC_OCEAN,
    BARCELONA,
    BARI,
    BAY_OF_BISCAY,
    BELGRADE,
    BERLIN,
    BLACK_SEA,
    BORDEAUX,
    BRUSSELS,
    BUCHAREST,
    BUDAPEST,
    CADIZ,
    CAGLIARI,
    CASTLE_DRACULA,
    CLERMONT_FERRAND,
    COLOGNE,
    CONSTANTA,
    DUBLIN,
    EDINBURGH,
    ENGLISH_CHANNEL,
    FLORENCE,
    FRANKFURT,
    GALATZ,
    GALWAY,
    GENEVA,
    GENOA,
    GRANADA,
    HAMBURG,
    IONIAN_SEA,
    IRISH_SEA,
    KLAUSENBURG,
    LE_HAVRE,
    LEIPZIG,
    LISBON,
    LIVERPOOL,
    LONDON,
    MADRID,
    MANCHESTER,
    MARSEILLES,
    MEDITERRANEAN_SEA,
    MILAN,
    MUNICH,
    NANTES,
    NAPLES,
    NORTH_SEA,
    NUREMBURG,
    PARIS,
    PLYMOUTH,
    PRAGUE,
    ROME,
    SALONICA,
    SANTANDER,
    SARAGOSSA,
    SARAJEVO,
    SOFIA,
    ST_JOSEPH_AND_ST_MARYS,
    STRASBOURG,
    SWANSEA,
    SZEGED,
    TOULOUSE,
    TYRRHENIAN_SEA,
    VALONA,
    VARNA,
    VENICE,
    VIENNA,
    ZAGREB,
    ZURICH,

    // Other "locations"
    CITY_UNKNOWN = 100,
    SEA_UNKNOWN = 101,
    HIDE = 102,
    DOUBLE_BACK_1 = 103,
    DOUBLE_BACK_2 = 104,
    DOUBLE_BACK_3 = 105,
    DOUBLE_BACK_4 = 106,
    DOUBLE_BACK_5 = 107,
    TELEPORT = 108,
    UNKNOWN_LOCATION = -1,
    NOWHERE = UNKNOWN_LOCATION,
} location_t;

#define MIN_MAP_LOCATION    (location_t) ADRIATIC_SEA
#define HOSPITAL_LOCATION   (location_t) ST_JOSEPH_AND_ST_MARYS
#define MAX_MAP_LOCATION    (location_t) ZURICH
#define NUM_MAP_LOCATIONS   ((int) ZURICH + 1)

///

region_t get_region(location_t loc);
region_t get_region(location_t loc) {
    switch (loc) {
        case CASTLE_DRACULA:
        case GALATZ:
        case VARNA:
        case BUCHAREST:
        case SOFIA:
        case BELGRADE:
        case SZEGED:
        case KLAUSENBURG:
        case CONSTANTA:
        case SALONICA:
        case VALONA:
        case ATHENS:
        case BLACK_SEA:
        case IONIAN_SEA:
            return REGION_1;

        case ST_JOSEPH_AND_ST_MARYS:
        case SARAJEVO:
        case BUDAPEST:
        case VIENNA:
        case ZAGREB:
        case MUNICH:
        case NUREMBURG:
        case FRANKFURT:
        case BERLIN:
        case LEIPZIG:
        case COLOGNE:
        case STRASBOURG:
        case ZURICH:
        case GENEVA:
        case MILAN:
        case BRUSSELS:
        case PARIS:
        case CLERMONT_FERRAND:
        case BARI:
        case NAPLES:
        case ROME:
        case VENICE:
        case FLORENCE:
        case GENOA:
        case MARSEILLES:
        case CAGLIARI:
        case TYRRHENIAN_SEA:
        case ADRIATIC_SEA:
            return REGION_2;

        case MANCHESTER:
        case GALWAY:
        case DUBLIN:
        case SWANSEA:
        case LIVERPOOL:
        case PLYMOUTH:
        case LONDON:
        case EDINBURGH:
        case AMSTERDAM:
        case HAMBURG:
        case PRAGUE:
        case LE_HAVRE:
        case ENGLISH_CHANNEL:
        case NORTH_SEA:
        case IRISH_SEA:
        case ATLANTIC_OCEAN:
            return REGION_3;

        case MADRID:
        case SARAGOSSA:
        case TOULOUSE:
        case GRANADA:
        case NANTES:
        case BORDEAUX:
        case SANTANDER:
        case LISBON:
        case CADIZ:
        case ALICANTE:
        case BARCELONA:
        case MEDITERRANEAN_SEA:
        case BAY_OF_BISCAY:
            return REGION_4;
        default: 
            return -1;
    }

    assert(0);
}
