#include <stdio.h>
#include <stdlib.h>
#include "ai.h"

int test_get_region(void);

int main(void) {

    int nLocations = test_get_region();
    if (nLocations < NUM_MAP_LOCATIONS) printf("Missing locations: %d\n", NUM_MAP_LOCATIONS - 1 - nLocations);

    else printf("Success, you have gotten all locations\n");
    return 0;
}




/* Function to test that we have all the locations */
int test_get_region(void)
{
    int counter = 0;

    for (location_t i = 0; i < MAX_MAP_LOCATION; i++)
    {
        region_t region = get_region(i);
        printf("Location: %d is in region %zu\n", i, region);
        if (region != -1) counter++;
    }
    return counter;
}
