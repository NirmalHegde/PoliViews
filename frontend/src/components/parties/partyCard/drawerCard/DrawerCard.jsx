import React from "react";
import { LinkBox, LinkOverlay, Heading, Text, Badge } from "@chakra-ui/react";

const BADGE_COLOR = {
  neutral: "yellow",
  positive: "green",
  negative: "red",
};

const DrawerCard = ({ badge, title, description, link }) => {
  return (
    <LinkBox as="article" maxW="sm" p="5" borderWidth="1px" rounded="md">
      <Heading size="md" my="2">
        <LinkOverlay href={link}>
          {title}
        </LinkOverlay>
      </Heading>
      <Text>
        {description}
      </Text>
      <Badge colorScheme={BADGE_COLOR[badge]}>{badge}</Badge>
    </LinkBox>
  );
};

export default DrawerCard;
