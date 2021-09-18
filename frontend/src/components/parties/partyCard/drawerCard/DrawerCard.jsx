import React from "react";
import { LinkBox, LinkOverlay, Heading, Text, Badge } from "@chakra-ui/react";

const DrawerCard = ({ badge, title, description, link }) => {
  const badgeColor = {
    neutral: "yellow",
    positive: "green",
    negative: "red",
  };

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
      <Badge colorScheme={badgeColor[badge]}>{badge}</Badge>
    </LinkBox>
  );
};

export default DrawerCard;
