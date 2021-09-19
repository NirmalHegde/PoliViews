import React, { useRef, useEffect, useState } from "react";
import axios from "axios";
import {
  Avatar,
  Box,
  CircularProgress,
  Button,
  Tooltip,
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

import DrawerCard from "./drawerCard/DrawerCard";
import styles from "./PartyCardStyles.js";

const INIT_TEXT = "Start by searching a hot topic for the 2021 election!";

const PartyCard = ({
  cards,
  short,
  name,
  leader,
  color,
  endColor,
  theme,
  picture,
  result,
  search,
  show,
}) => {
  const { center, descriptionText } = styles;

  const [transition, setTransition] = useState("start");
  const [loading, setLoading] = useState(false);
  const [links, setLinks] = useState([]);
  const btnRef = useRef();
  const { onOpen, isOpen, onClose } = useDisclosure();

  useEffect(() => {
    if (cards === true) {
      setTimeout(() => {
        setTransition("end");
      }, 500);
    }
  }, [cards]);

  const handleDrawerOpen = async () => {
    setLoading(true);
    onOpen();

    const response = await axios
      .get(
        `https://poliviews-api.herokuapp.com/api/related-articles?query=${search}&party=${short}`
      )
      .then((res) => {
        return res.data[short];
      })
      .catch((err) => {
        console.log(err);
        return null;
      });

    setLinks(response);
    setLoading(false);
  };

  return (
    <div>
      {cards && (
        <Box
          bg="#FFFFFF"
          maxH="37vh"
          minW="sm"
          p={4}
          borderRadius="lg"
          boxShadow="base"
          style={styles[transition]}
        >
          <Grid
            templateRows="repeat(2, 0.3fr)"
            templateColumns="repeat(5, 1fr)"
            gap={4}
          >
            <GridItem colSpan={1} style={center}>
              <Tooltip
                hasArrow
                placement="top"
                bg={color}
                label={leader}
                aria-label="A tooltip"
              >
                <Avatar
                  p={1}
                  backgroundColor={color}
                  name={name}
                  src={picture}
                  size="xl"
                />
              </Tooltip>
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
      )}

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
          <DrawerBody>
            {loading && (
              <div style={center}>
                <CircularProgress isIndeterminate color="green.300" />
              </div>
            )}
            {!loading &&
              links &&
              links.map((link) => (
                <DrawerCard
                  badge={link.sentiment}
                  title={link.title}
                  link={link.link}
                />
              ))}
            {!loading && !links && <Text>No articles found...</Text>}
          </DrawerBody>
        </DrawerContent>
      </Drawer>
    </div>
  );
};

export default PartyCard;
