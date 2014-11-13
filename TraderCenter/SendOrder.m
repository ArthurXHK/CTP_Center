function orderref = SendOrder(account, inst, direction, offset, volume, price)

orderref = TraderMain(4, account, inst, num2str(direction), num2str(offset), volume, price);

end

