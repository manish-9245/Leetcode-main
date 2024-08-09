locals {
  ip_port_map = {
    "ip1/32" = "port1",
    "ip2/32" = "port2",
    "ip3/32" = "port1",
    "ip4/32" = "port2"
  }

  egress_rules = flatten([
    for ip, port in local.ip_port_map : {
      cidr_block = ip
      from_port  = port
      to_port    = port
    }
  ])
}

resource "aws_security_group_rule" "egress_rules" {
  count = length(local.egress_rules)

  type              = "egress"
  from_port         = local.egress_rules[count.index].from_port
  to_port           = local.egress_rules[count.index].to_port
  protocol          = "tcp"
  cidr_blocks       = [local.egress_rules[count.index].cidr_block]
  security_group_id = aws_security_group.example.id
}
