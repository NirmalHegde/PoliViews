import React from "react";
import { SimpleGrid } from "@chakra-ui/layout";

import PartyCard from "./partyCard/PartyCard";

const Parties = () => {
  const PARTY_INFO = [
    { name: "Liberal Party", color: "#BC0817" },
    { name: "Conservative Party", color: "#0C499C" },
    { name: "New Democratic Party", color: "#FA5D26" },
  ];

  return (
    <SimpleGrid columns={3} spacing={10}>
      {PARTY_INFO.map((party) => (
        <PartyCard name={party.name} color={party.color} />
      ))}
    </SimpleGrid>
  );
};

export default Parties;
