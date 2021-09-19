import React, { useRef } from "react";
import {
  Avatar,
  Box,
  Button,
  Stack,
  Skeleton,
  Heading,
  Text,
  Grid,
  GridItem,
  Drawer,
  DrawerBody,
  DrawerHeader,
  DrawerOverlay,
  DrawerContent,
  DrawerCloseButton,
  useDisclosure,
} from "@chakra-ui/react";
import { ArrowForwardIcon } from "@chakra-ui/icons";

import styles from "./PartyCardStyles.js";

const INIT_TEXT = "Start by searching a hot topic for the 2021 election!";

const PartyCard = ({
  name,
  color,
  endColor,
  theme,
  picture,
  result,
  search,
  show,
}) => {
  const { center, descriptionText } = styles;

  const { onOpen, isOpen, onClose } = useDisclosure();
  const btnRef = useRef();

  const handleDrawerOpen = () => {
    onOpen();
  };

  return (
    <div>
      <Box
        bg="#FFFFFF"
        maxH="38vh"
        minW="sm"
        p={4}
        borderRadius="lg"
        boxShadow="base"
      >
        <Grid
          templateRows="repeat(2, 0.3fr)"
          templateColumns="repeat(5, 1fr)"
          gap={4}
        >
          <GridItem colSpan={1} style={center}>
            <Avatar
              p={1}
              backgroundColor={color}
              name={name}
              src={picture}
              size="xl"
            />
          </GridItem>
          <GridItem colSpan={4} style={center}>
            <Heading as="h1" size="lg" color="#2D3748">
              {name}
            </Heading>
          </GridItem>
          <GridItem colSpan={5}>
            {!show && (
              <Stack>
                {[...Array(6)].map((e, i) => (
                  <Skeleton key={i} endColor={endColor} height="1rem" />
                ))}
              </Stack>
            )}
            {show && (
              <Stack>
                <Text color="#696E78" style={descriptionText}>
                  {result ? result : INIT_TEXT}
                </Text>
                {result && (
                  <Button
                    ref={btnRef}
                    onClick={() => handleDrawerOpen()}
                    rightIcon={<ArrowForwardIcon />}
                    colorScheme={theme}
                    variant="ghost"
                  >
                    See similar articles
                  </Button>
                )}
              </Stack>
            )}
          </GridItem>
        </Grid>
      </Box>

      <Drawer placement="right" onClose={onClose} isOpen={isOpen}>
        <DrawerOverlay />
        <DrawerContent>
          <DrawerHeader borderBottomWidth="1px">
            <Grid
              templateRows="repeat(1, 0.3fr)"
              templateColumns="repeat(10, 1fr)"
              gap={4}
            >
              <GridItem colSpan={9}>
                <Heading size="md">
                  Related articles to "{search}" for the {name}:
                </Heading>
              </GridItem>
              <GridItem colSpan={1}>
                <DrawerCloseButton />
              </GridItem>
            </Grid>
          </DrawerHeader>
          <DrawerBody></DrawerBody>
        </DrawerContent>
      </Drawer>
    </div>
  );
};

export default PartyCard;
