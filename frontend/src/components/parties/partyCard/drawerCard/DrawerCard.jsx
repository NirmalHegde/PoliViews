import React from "react";
import { LinkBox, LinkOverlay, Text, Badge } from "@chakra-ui/react";

const BADGE_COLOR = {
  neutral: "yellow",
  positive: "green",
  negative: "red",
};

const DrawerCard = ({ badge, title, link }) => {
  return (
    <div>
      <LinkBox _hover={{ background: "#EDF1F5", transition: "0.5s" }} as="article" maxW="sm" p="5" borderWidth="1px" rounded="md">
        <Text size="md" my="2">
          <LinkOverlay href={link} target="_blank">{title}</LinkOverlay>
        </Text>
        <Badge colorScheme={BADGE_COLOR[badge]}>{badge}</Badge>
      </LinkBox>
      <br />
    </div>
  );
};

export default DrawerCard;
